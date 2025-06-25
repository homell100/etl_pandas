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
    

def read_users_excel(file_path=f"{data_dir}/users.csv"):
    data_types = {
        'id': np.int16,
        'email': 'S10'
    }
    try:
        excel_dfs = pd.read_excel(file_path, 
                                    sheet_name=[0,1],
                                    parse_dates=["signup_date"],
                                    dtype=data_types)
        print(excel_dfs)
        return pd.concat(excel_dfs.values(), ignore_index=True)
    except FileNotFoundError as e:
        print(f"Excel file not found in {file_path}")
    return None

if __name__ == "__main__":
    print(read_products_csv())
    print(read_users_excel())