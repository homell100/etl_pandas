import os
import pandas as pd
import numpy as np
from pathlib import Path

current_path = Path(__file__).resolve()
root_path = current_path.parent.parent
data_dir = os.path.join(root_path, "data", "input")


def read_products_csv(file_path=f"{data_dir}/products.csv"):
    data_types = {
        "product_id": np.int16,
        "name": 'S10',
        "price": np.float32
    }
    try:
        products_df = pd.read_csv(file_path,
                                    parse_dates=[3],
                                    dtype=data_types)
        return products_df
    except FileNotFoundError as e:
        print(f"Csv file not found in {file_path}")
    return None
    

def read_users_excel():
    excel_dfs = pd.read_excel(f"{data_dir}/users.xlsx", sheet_name=[0,1])
    return pd.concat(excel_dfs.values())

if __name__ == "__main__":
    print(read_products_csv())
    print(read_users_excel())