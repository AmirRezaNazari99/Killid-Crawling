import psycopg2


def create_table():

    conn = psycopg2.connect(
        host="localhost",
        database="junior",
        user="postgres",
        password="postgres",
        port="45432"
    )
    cur = conn.cursor()

    try:
        delete = """DROP TABLE property;"""
        cur.execute(delete)
        conn.commit()

    except:
        pass

    command = """CREATE TABLE Property(
                id SERIAL PRIMARY KEY,
                Price VARCHAR(255) ,
                Location VARCHAR(255),
                Type VARCHAR(50),
                Size VARCHAR(255),
                Bedrooms VARCHAR(255),
                Parking VARCHAR(255)
            )"""

    # command = """DROP TABLE property;"""
    # cur.execute(command)

    try:
        cur.execute(command)
    except:
        print("Table has already existed")

    conn.commit()
    return conn, cur


# create_table()
