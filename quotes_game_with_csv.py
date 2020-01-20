import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader
import os


LOCATION = (os.path.dirname(os.path.realpath(__file__)) + "\\csv_scraper_quotes.csv")
BASE_URL = "http://quotes.toscrape.com"


def read_quotes(filename):
    with open (filename, "r", encoding="utf-8") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)


def start_game(quotes):
    guess = ''
    remaining_guesses = 4
    quote = choice(quotes)
    
    print("\nHere's a quote: " + quote["text"] + "\n")

    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        guess = input(f"You have {remaining_guesses} guesses remaining. Who said this quote?: ")
        if guess.lower() == quote["author"].lower():
            print("YOU WIN!")
            break
        remaining_guesses -= 1
        print_hint(quote, remaining_guesses)

    again = ''
    while again.lower() not in ('y', 'yes', 'n', 'no'):
        again = input("Would you like to play again (y/n)? ")
    if again.lower() in ('yes', 'y'):
        return start_game(quotes) #Calling yourself
    else:
        print("OK, GOODBYE!")


def print_hint(quote, remaining_guesses):
    if remaining_guesses == 3:
        res = requests.get(f"{BASE_URL}{quote['bio-link']}")
        soup = BeautifulSoup(res.text, "html.parser")
        birth_date = soup.find(class_="author-born-date").get_text()
        birth_place = soup.find(class_="author-born-location").get_text()
        print(f"Here's a hint.. The author was born on {birth_date} {birth_place}")
    elif remaining_guesses == 2:
        print(f"Here's a hint.. The author's first name starts with: {quote['author'][0]}")
    elif remaining_guesses == 1:
        last_initial = quote["author"].split(" ")[1][0]
        print(f"Here's a hint.. The author's last name starts with: {last_initial}")
    else:
        print(f"Sorry you ran out of guesses. The answer was {quote['author']}")


#run game
quotes = read_quotes(LOCATION)
start_game(quotes)