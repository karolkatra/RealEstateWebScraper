import requests
from bs4 import BeautifulSoup
import sqlite3


def clear_price(price):
    return price.replace('\xa0', '').replace('zł', '').strip()

def insert_into_database(link, price, meters, location):
    conn = sqlite3.connect('mieszkania.db')

    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mieszkania (
        id INTEGER PRIMARY KEY,
        link TEXT,
        price TEXT,
        meters TEXT,
        location TEXT
        )
    ''')

    link = f"https://www.otodom.pl{link}"
    price = f"Cena: {clear_price(price)} zł"
    meters = f"Metraż: {meters}"
    location = f"Lokalizacja: {location}"

    cursor.execute("INSERT INTO mieszkania (link, price, meters, location) VALUES (?, ?, ?, ?)", (link, price, meters, location))

    conn.commit()
    conn.close()


def display_database_content():
    conn = sqlite3.connect("mieszkania.db")
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM mieszkania")
    except sqlite3.OperationalError as e:
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
    conn = sqlite3.connect('mieszkania.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM mieszkania")

    conn.commit()
    conn.close()

def get_page_content(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Błąd podczas pobierania strony: {e}")
        return None


def parse_html(content):
    properties = []
    clear_database()

    if content:
        soup = BeautifulSoup(content, 'html.parser')

        listing_items = soup.select('[data-cy="listing-item"]')

        for item in listing_items:
            link = item.select_one('a')['href']
            location = item.select_one('p[title]').get_text()

            spans = item.select('.css-1cyxwvy.ei6hyam2')

            if len(spans) >= 4:
                price = spans[0].get_text(strip=True)
                meters = spans[3].get_text(strip=True)

                insert_into_database(link, price, meters, location)

                properties.append({
                    'link': link,
                    'price': price,
                    'meters': meters,
                    'location':location
                })

    return properties


if __name__ == "__main__":
    url_to_scrape = "https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/wiele-lokalizacji?limit=36&ownerTypeSingleSelect=ALL&priceMax=650000&areaMin=45&locations=%5Bmazowieckie%2Fwarszawa%2Fwarszawa%2Fwarszawa%2Fzoliborz%2Cmazowieckie%2Fwarszawa%2Fwarszawa%2Fwarszawa%2Fwola%2Cmazowieckie%2Fwarszawa%2Fwarszawa%2Fwarszawa%2Fochota%2Cmazowieckie%2Fwarszawa%2Fwarszawa%2Fwarszawa%2Fursynow%2Cmazowieckie%2Fwarszawa%2Fwarszawa%2Fwarszawa%2Fmokotow%5D&roomsNumber=%5BTHREE%2CFOUR%2CFIVE%2CSIX_OR_MORE%2CTWO%5D&by=DEFAULT&direction=DESC&viewType=listing"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    page_content = get_page_content(url_to_scrape, headers)
    scraped_properties = parse_html(page_content)

    for prop in scraped_properties:
        print(f"https://www.otodom.pl{prop['link']}, Cena: {prop['price']}, Metraż: {prop['meters']}, Lokalizacja: {prop['location']}")

    display_database_content()






