import requests
from bs4 import BeautifulSoup


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

    if content:
        soup = BeautifulSoup(content, 'html.parser')

        listing_items = soup.select('[data-cy="listing-item"]')

        for item in listing_items:
            link = item.select_one('a')['href']
            location = item.select_one('p[title]').get_text()

            # Zmieniłem selektor na odpowiedni
            spans = item.select('.css-1cyxwvy.ei6hyam2')

            if len(spans) >= 4:
                price = spans[0].get_text(strip=True)
                meters = spans[3].get_text(strip=True)

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
