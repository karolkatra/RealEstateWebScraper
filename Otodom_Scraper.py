from bs4 import BeautifulSoup
from Database import insert_into_database
import requests


def get_page_content(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Błąd podczas pobierania strony: {e}")
        return None
def parse_html_otodom(content):
    if content:
        soup = BeautifulSoup(content, 'html.parser')
        listing_items = soup.select('[data-cy="listing-item"]')

        for item in listing_items:
            link = item.select_one('a')['href']
            location = item.select_one('p[title]').get_text()

            spans = item.select('.css-1cyxwvy.ei6hyam2')

            if len(spans)>= 4:
                price = spans[0].get_text(strip=True)
                meters = spans[3].get_text(strip=True)

                insert_into_database(link, price, meters, location)
