import pandas as pd
import os

ROOT = os.path.dirname(os.path.abspath(__file__))


def read_excel(path: str) -> pd.DataFrame:
    """Read the excel file from the path"""
    df = pd.read_excel(path)
    return df


def transform_data() -> dict:
    """Transforms the existing files in input and returns a dictionary with dataframes of their respective files."""
    # Read all the existing files in the input.
    files = os.listdir(ROOT + "/input")

    dict_of_dfs = {}

    # We iterate over the files in the folder.
    for file in files:
        # We extract only Victims_Age_by_Offense_Category_2022.xlsx from the .zip file.
        if file.endswith(".xlsx"):
            df = read_excel(ROOT + "/input/" + file)
            # We remove the first two rows.
            df_keys_1 = df.iloc[2:3, 0:2].values.flatten().tolist()

            # We remove the first two rows.
            df_keys_2 = df.iloc[3:4, 2:].values.flatten().tolist()

            # Union the two lists.
            df_keys = df_keys_1 + df_keys_2

            # Replace the \n with spaces.
            df_keys = [key.replace("\n", " ").replace("Victims1", "Victims") for key in df_keys]
            
            # We use the list as keys for our dataframe and read the entire dataframe.
            df = pd.read_excel(ROOT + "/input/" + file, skiprows=12, names=df_keys)

            # We remove the last row.
            df = df.iloc[:-1]

            # We remove the second column.
            df = df.drop(df.columns[1], axis=1)

            # File name without extension.
            file_name = file.split(".")[0]

            # save the dataframe to a dictionary.
            dict_of_dfs[file_name] = df

    return dict_of_dfs