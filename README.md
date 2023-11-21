# RealEstateWebScraper

Overview

This project is a web scraper designed to extract real estate information from the Otodom website. The scraper retrieves data on apartments for sale in Warsaw, Mazowieckie, within a specified price range and minimum area. The extracted data includes the property link, price, area, and location.

The project consists of three main components:

- Main Script: The entry point of the application, where the scraping process is initiated.
- Otodom Scraper Module: Contains functions to fetch webpage content, parse HTML using BeautifulSoup, and insert the extracted data into a PostgreSQL database.
- Database Module: Manages the PostgreSQL database, including table creation, data insertion, display, and clearing.
# Programs Used

- Python
- PostgreSQL

# Installation

**Dependencies**

Before running the scraper, ensure that the required Python libraries are installed. You can install them using the following commands:

- pip install requests
- pip install beautifulsoup4
- pip install psycopg2

**Database Setup**

The project utilizes PostgreSQL as the database management system. Before running the scraper, set up a PostgreSQL database. Create a database named "postgres" (or your preferred name) and update the database connection parameters in the Database.py file.

```
conn = psycopg2.connect(
        dbname="Your Database name", user="postgres", password="Your Password", host="localhost"
    )
```

# Customizing Otodom URL

**Changing the Otodom URL**
The Otodom URL used in the main.py script specifies the initial configuration for the scraper. You can customize the URL to suit your specific requirements by modifying the otodom_url_to_scrape variable in the main.py script.

```
otodom_url_to_scrape = "https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/mazowieckie/warszawa/warszawa/warszawa?limit=72&ownerTypeSingleSelect=ALL&priceMax=600000&areaMin=49&by=DEFAULT&direction=DESC&viewType=listing&page="
```
**Queries that can be adjusted**

- priceMax=600000: Maximum price filter,
- areaMin=49: Minimum area filter,

To change the city you have to change the city and voivodeship

For example:
```
otodom_url_to_scrape = "https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/malopolskie/krakow/krakow/krakow?limit=72&ownerTypeSingleSelect=ALL&priceMax=800000&areaMin=49&by=DEFAULT&direction=DESC&viewType=listing&page="
```
This will search the Real Estates in Cracow and the maximum price is set to 800000PLN


  
