# practice quotes scraper

import requests
from bs4 import BeautifulSoup
import csv

def get_quotes():
    response = requests.get("http://quotes.toscrape.com/")
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.select(".quote")

    with open('quotes.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, quotechar='"', quoting=csv.QUOTE_ALL)
        for quote_div in quotes:
            quote = quote_div.find("span", class_="text").text.strip() # get the quote
            quote = clean_quotes(quote)
            author = quote_div.find("small", class_="author").text # get the author's name
            tags = quote_div.find_all("a", class_="tag") # get any associated tags
            tag_list = [tag.text.strip() for tag in tags] # list comprehension to create a list of tags for each quote
            tag_str = ", ".join(tag_list) # join the tag_list as a string to help with csv writing cleanly

            print(quote, author, tag_str)

            writer.writerow([quote, author, tag_str])

def clean_quotes(raw_quote: str) -> str:
    return raw_quote.replace("“", '').replace("”", '').replace("‘", "").replace("’", "")


if __name__ == "__main__":
    get_quotes()
