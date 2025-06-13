import os
import pandas as pd
import json
import pyarrow as pa
import pyarrow.parquet as pq
import xml.etree.ElementTree as ET

# Directory setup
data_dir = "../data/input"
os.makedirs(data_dir, exist_ok=True)

# 1. products.csv
products_df = pd.DataFrame({
    "product_id": [101, 102, 103],
    "name": ["Widget", "Gadget", "Doohickey"],
    "price": [19.99, 29.99, 9.99]
})
products_df.to_csv(f"{data_dir}/products.csv", index=False)

# 2. users.xlsx
users_df = pd.DataFrame({
    "id": [1, 2, 3],
    "email": ["alice@example.com", "bob@example.com", "carol@example.com"],
    "signup_date": ["2023-01-01", "2023-02-15", "2023-03-10"]
})
users_df.to_excel(f"{data_dir}/users.xlsx", index=False)

# 3. orders.json
orders_data = [
    {
        "order_id": 201,
        "user_id": 1,
        "date": "2023-04-01",
        "items": [
            {"product_id": 101, "quantity": 2},
            {"product_id": 102, "quantity": 1}
        ]
    },
    {
        "order_id": 202,
        "user_id": 2,
        "date": "2023-04-03",
        "items": [
            {"product_id": 103, "quantity": 5}
        ]
    }
]
with open(f"{data_dir}/orders.json", "w") as f:
    json.dump(orders_data, f, indent=2)

# 4. transactions.parquet
transactions_df = pd.DataFrame({
    "transaction_id": [301, 302],
    "user_id": [1, 3],
    "amount": [49.98, 9.99],
    "timestamp": ["2023-04-01T10:00:00", "2023-04-05T14:30:00"]
})
table = pa.Table.from_pandas(transactions_df)
pq.write_table(table, f"{data_dir}/transactions.parquet")

# 5. catalog.xml
catalog = ET.Element("catalog")
for pid, name, price in zip(products_df["product_id"], products_df["name"], products_df["price"]):
    product = ET.SubElement(catalog, "product", id=str(pid))
    ET.SubElement(product, "name").text = name
    ET.SubElement(product, "price").text = str(price)

tree = ET.ElementTree(catalog)
tree.write(f"{data_dir}/catalog.xml", encoding="utf-8", xml_declaration=True)

print("All files created successfully.")
