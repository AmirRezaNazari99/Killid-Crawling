import pandas as pd
from selenium import webdriver

from Crawling import parse_page
from db_connection import create_table
from db_filling import add_data_to_db
from db_query import query_locations

conn, cur = create_table()
driver = webdriver.Chrome()

for page in range(9):
    parsed = parse_page(page, driver)
    add_data_to_db(parsed, conn, cur)


command = "SELECT * FROM Property"
cur.execute(command)
property_records = cur.fetchall()

data_df = pd.DataFrame(columns=['Price','Location','Type','Size','Bedrooms','Parking'])
for row in property_records:
    dic = {
        'Price': row[1],
        'Location': row[2],
        'Type': row[3],
        'Size': row[4],
        'Bedrooms': row[5],
        'Parking': row[6],
    }

    data_df = data_df._append(dic, ignore_index=True)

query_locations(data_df)
