import requests
from bs4 import BeautifulSoup
from random import choice
from termcolor import colored
#from time import sleep

BASE_URL = "http://quotes.toscrape.com"


def scrape_quotes():
    all_quotes = []
    url = "/page/1"
    while url:
        res = requests.get(f"{BASE_URL}{url}")
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.find_all(class_="quote")
        print(f"Now Scraping... {BASE_URL}{url}")
        
        for quote in quotes:
            all_quotes.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio-link": quote.find("a")["href"]
            })
        #sleep(2) #politeness is not overrated.
        next_button = soup.find(class_="next")
        url = next_button.find("a")["href"] if next_button else None
    return all_quotes


def start_game(quotes):
    guess = ''
    remaining_guesses = 4
    quote = choice(quotes)

    print("\nHere's a quote: \n" + colored(quote["text"], color="green") + "\n")

    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        guess = input(f"You have {remaining_guesses} guesses remaining. Who said this?: ")
        if guess.lower() == quote["author"].lower():
            print(colored("\nYOU WIN!\n", color="blue"))
            break
        remaining_guesses -= 1
        print_hint(quote, remaining_guesses)

    again = ''
    while again.lower() not in ('y', 'yes', 'n', 'no'):
        again = input("Would you like to play again? Y/N ")
    if again.lower() in ('yes', 'y'):
        return start_game(quotes) #Calling yourself
    else:
        print("\nOK, GOODBYE!")


def print_hint(quote, remaining_guesses):
    if remaining_guesses == 3:
        res = requests.get(f"{BASE_URL}{quote['bio-link']}")
        soup = BeautifulSoup(res.text, "html.parser")
        birth_date = soup.find(class_="author-born-date").get_text()
        birth_place = soup.find(class_="author-born-location").get_text()
        print(f"\nHere's a hint... The author was born on {birth_date} {birth_place}.\n")
    elif remaining_guesses == 2:
        print(f"\nHere's a hint... The author's first name starts with: {quote['author'][0]}.\n")
    elif remaining_guesses == 1:
        last_initial = quote["author"].split(" ")[1][0]
        print(f"\nHere's a hint... The author's last name starts with: {last_initial}.\n")
    else:
        print(colored(f"\nSorry, you ran out of guesses. The answer was {quote['author']}\n", color="red"))


#Running the game
quotes = scrape_quotes()
start_game(quotes)
