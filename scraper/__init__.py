from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

load_dotenv()

URL = os.getenv("URL")
ROOT = os.path.dirname(os.path.abspath(__file__))


def donwload_data(page) -> bool:
    """Download the data from the page
    :param page: playwrigh
    """
    page.click('text="Documents & Downloads"')

    # We select the option 'Victims' from the list of choices in the xpath //*[@id="dwnnibrs-download-select"]/button.
    page.locator('//*[@id="dwnnibrs-download-select"]/button').click()
    page.click('text="Victims"')

    # We select the option 2022
    page.locator('//*[@id="dwnnibrscol-year-select"]/button').click()
    page.click('text="2022"')

    # We select location Florida
    page.locator('//*[@id="dwnnibrsloc-select"]/button').click()
    page.click('text="Florida"')

    # storage folder if it doesn't exist.
    os.makedirs(os.path.dirname(ROOT +"/storage/"), exist_ok=True)

    # We download the file
    with page.expect_download() as download_info:
        page.click('//*[@id="nibrs-download-button"]')
    
    # We save the file with its own name.
    download = download_info.value
    download.save_as(ROOT + "/storage/" + download.suggested_filename)


def start_scraper() -> bool:
    """Start the scraper and download the data from the page in the URL variable."""
    with sync_playwright() as p:
        # headless=False to see the browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(URL)
        
        # Download data
        donwload_data(page)
        browser.close()
    return True
