# practice file for scraping quotes

import requests
from bs4 import BeautifulSoup

def scrape_quotes(url="https://quotes.toscrape.com"):
    response = requests.get(url)
    response.raise_for_status()  # Raise error if request fails

    soup = BeautifulSoup(response.text, "html.parser") # create bs4 object

    # select quotes from the bs4 object
    quotes = soup.select(".quote")
    entry = 1 # create count variable

    for quote_div in quotes: # cycle through the quotes and save the text/author
        text = quote_div.find("span", class_="text").get_text(strip=True)
        author = quote_div.find("small", class_="author").get_text(strip=True)

        # print each line
        print(f"{entry}. {text} -{author}")
        entry += 1 # increment count

# simply prints the quotes
if __name__ == "__main__":
    scrape_quotes()