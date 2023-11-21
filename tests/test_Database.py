import unittest
from Database import insert_into_database, display_database_content, clear_database


class TestDatabaseOperations(unittest.TestCase):
    def test_insert_into_database(self):
        link = "/example-link"
        price = "Cena: 500000 zł"
        meters = "Metraż: 75"
        location = "Warsaw"
        insert_into_database(link, price, meters, location)


    def test_display_database_content(self):
        link = "/example-link"
        price = "Cena: 500000 zł"
        meters = "Metraż: 72"
        location = "Warsaw"
        insert_into_database(link, price, meters, location)

        display_database_content()

    def test_clear_database(self):
        link = "/example-link"
        price = "Cena: 500000 zł"
        meters = "Metraż: 70"
        location = "Warsaw"
        insert_into_database(link, price, meters, location)

        clear_database()

if __name__ == '__main__':
    unittest.main()