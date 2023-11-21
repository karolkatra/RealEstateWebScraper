import unittest
from Otodom_Scraper import get_page_content

class TestScraperFunctions(unittest.TestCase):
    def test_get_page_content_success(self):
        url = "https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/mazowieckie/warszawa/warszawa/warszawa?limit=72&ownerTypeSingleSelect=ALL&priceMax=600000&areaMin=49&by=DEFAULT&direction=DESC&viewType=listing&page="
        headers = {'User-Agent': 'Test User Agent'}
        content = get_page_content(url, headers)
        self.assertIsNotNone(content)

    def test_get_page_content_failure(self):
        url = "https://www.invalidurl.com"
        headers = {'User-Agent': 'Test User Agent'}
        content = get_page_content(url, headers)
        self.assertIsNone(content)

if __name__ == '__main__':
    unittest.main()