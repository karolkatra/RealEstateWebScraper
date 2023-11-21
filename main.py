from Otodom_Scraper import parse_html_otodom
from Otodom_Scraper import get_page_content



if __name__ == '__main__':
    otodom_url_to_scrape = "https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/mazowieckie/warszawa/warszawa/warszawa?limit=72&ownerTypeSingleSelect=ALL&priceMax=600000&areaMin=49&by=DEFAULT&direction=DESC&viewType=listing&page="
    otodom_pages = 3
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }




    for otodom_pages in range(1, otodom_pages + 1):
        otodom_url = f"{otodom_url_to_scrape}{otodom_pages}"
        otodom_content = get_page_content(otodom_url, headers)
        if otodom_content:
            parse_html_otodom(otodom_content)
