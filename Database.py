import psycopg2

def clear_price(price):
    return price.replace('\xa0', '').replace('zł', '').strip()

def insert_into_database(link, price, meters, location):
    conn = psycopg2.connect(
        dbname="postgres", user="postgres", password="karol123", host="localhost"
    )

    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mieszkania (
        id SERIAL PRIMARY KEY,
        link TEXT,
        price TEXT,
        meters TEXT,
        location TEXT
        )
    ''')

    link = f"https://www.otodom.pl{link}"
    price = f"Cena: {clear_price(price)}"
    meters = f"Metraż: {meters}"
    location = f"Lokalizacja: {location}"

    cursor.execute("SELECT id FROM mieszkania WHERE link = %s", (link,))
    existing_record = cursor.fetchone()

    if not existing_record:
        cursor.execute("INSERT INTO mieszkania (link, price, meters, location) VALUES (%s, %s, %s, %s)", (link, price, meters, location))

    conn.commit()
    conn.close()



def display_database_content():
    conn = psycopg2.connect(
        dbname="postgres", user="postgres", password="karol123", host="localhost"
    )
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM mieszkania")
    except psycopg2.Error as e:
        print(f"Error: {e}")
        print("Table 'mieszkania' does not exist yet")
        return
    rows = cursor.fetchall()

    if not rows:
        print("No data in the 'mieszkania' table.")
    else:
        for row in rows:
            print(row)
    conn.close()

def clear_database():
    conn = psycopg2.connect(
        dbname="postgres", user="postgres", password="karol123", host="localhost"
    )
    cursor = conn.cursor()

    cursor.execute("DELETE FROM mieszkania")

    conn.commit()
    conn.close()