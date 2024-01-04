import pandas as pd
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

def load_data(dict_of_dfs:dict) -> bool:
    """Save the dataframe to a CSV file."""

    for key, df in dict_of_dfs.items():

        # We create the output folder if it doesn't exist.
        if not os.path.exists(ROOT + "/output"):
            os.makedirs(ROOT + "/output")
        
        df.to_csv(ROOT + "/output/" + key + ".csv", index=False)
    return True