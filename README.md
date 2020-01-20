
# Quotes Guessing Game!

[Repl.it demo here!](https://quotes-game.chrispinkney.repl.run) 

A quotes-based guessing game filled with data pulled from the a friendly scraping site.

The player has four guesses to figure out which famous person said the quote randomly selected from their website.

### Offline Mode
An offline mode is available for the quote guessers concerned with the bandwidth requirement of scraping 10<sup>2</sup> + 1 worth of quotes. 
Simply download (or git clone the repo) both 

 - [quotes_game_with_csv.py](https://github.com/chrispinkney/quotes-game/blob/master/quotes_game_with_csv.py)
 - [csv_scraper_quotes.csv](https://github.com/chrispinkney/quotes-game/blob/master/csv_scraper_quotes.csv "csv_scraper_quotes.csv")

and run 

> mkdir quotes

> cd quotes

> python quotes_game_with_csv.py

in your terminal. The provided csv_scraper_quotes.csv is up to date as of [20-Jan-2020](https://www.timeanddate.com/date/durationresult.html?m1=1&d1=20&y1=2020&m2=1&d2=20&y2=2020&ti=on).

## Technology
The game is written in Python along with the Requests library to pull the data, and the Beautiful Soup library to scrape the information provided by [http://quotes.toscrape.com](http://quotes.toscrape.com/).
