#This module scrapes the quotes to a local csv file for offline-use. Run this file before running quotes_game_with_csv.py


import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictWriter
#from time import sleep
import os

LOCATION = (os.path.dirname(os.path.realpath(__file__)) + "\\csv_scraper_quotes.csv")
BASE_URL = "http://quotes.toscrape.com"


def scrape_quotes():
    all_quotes = []
    url = "/page/1"
    while url:
        res = requests.get(f"{BASE_URL}{url}")
        res.encoding = "utf-8"
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.find_all(class_="quote")
        print(f"Now Scraping... {BASE_URL}{url}")
        
        for quote in quotes:
            all_quotes.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio-link": quote.find("a")["href"]
            })
        #sleep(1) #politeness is not overrated.
        next_button = soup.find(class_="next")
        url = next_button.find("a")["href"] if next_button else None
    return all_quotes


#write quotes to a csv file
def write_quotes(quotes):
    with open(LOCATION, "w", encoding="utf-8", newline='') as file:
        headers = ["text", "author", "bio-link"]
        csv_writer = DictWriter(file, fieldnames = headers)
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)

#scrape quotes
quotes = scrape_quotes()
write_quotes(quotes)