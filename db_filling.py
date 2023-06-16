import psycopg2

def add_data_to_db(parsed, conn, cur):
    for feature in parsed:
        try:
            price = feature["price"]
            location = feature["location"]
            type_ = feature["type"]
            size = feature["size"]
            bedrooms = feature["bedrooms"]
            parking = feature["parking"]
            insert_query = """ INSERT INTO Property (Price, Location, Type, Size, Bedrooms, Parking) VALUES (%s,%s,%s,%s,%s,%s)"""
            record_to_insert = (price, location, type_, size, bedrooms, parking)
            cur.execute(insert_query, record_to_insert)
            conn.commit()

            count = cur.rowcount
            print(count, "Record inserted successfully into Property table")

        except (Exception, psycopg2.Error) as error:
            print("Failed to insert record into Property table", error)
