import os
import zipfile

# We extract the data from the .zip file loaded by the scraper into the 'storage' folder.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def extract_data() -> bool:
    """Extract the data from the .zip file loaded by the scraper into the 'storage' folder."""
    # Extract all the names from the 'scraper/storage' folder.
    files = os.listdir(ROOT + "/scraper/storage")

    # We iterate over the files in the folder.
    for file in files:
        # We extract only Victims_Age_by_Offense_Category_2022.xlsx from the .zip file.
        if file.endswith(".zip"):
            with zipfile.ZipFile(ROOT + "/scraper/storage/" + file, 'r') as zip_ref:
                zip_ref.extract("Victims_Age_by_Offense_Category_2022.xlsx", ROOT + "/etl/input/")
    return True