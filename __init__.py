from scraper import start_scraper
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data
from utils.loger import create_loger


def main():
    loger = create_loger()
    scraper = start_scraper()

    loger.info("ETL process started.")
    if scraper:
        loger.info("Scraper successfully.")
        extract = extract_data()
        if extract:
            loger.info("Extract successfully.")
            transform = transform_data()
            if transform:
                loger.info("Transform successfully.")
                load = load_data(transform)
                if load:
                    loger.info("Load successfully.")
                else:
                    loger.error("Load failed.")
            else:
                loger.error("Transform failed.")
        else:
            loger.error("Extract failed.")

if __name__ == "__main__":
    main()