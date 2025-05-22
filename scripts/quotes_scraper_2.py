# practice quotes scraper

import requests
from bs4 import BeautifulSoup

def get_quotes():
    response = requests.get("http://quotes.toscrape.com/")
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser") #

    quotes = soup.select(".quote")

    for quote_div in quotes:
        quote = quote_div.find("span", class_="text").text # get the quote
        author = quote_div.find("small", class_="author").text # get the author's name
        tags = quote_div.find_all("a", class_="tag") # get any associated tags
        tag_list = [tag.text for tag in tags] # list comprehension to create a list of tags for each quote

        # print the information for each quote to the terminal
        print(f"{quote} by {author} | {tag_list}") # tag list prints as a list of strings


if __name__ == "__main__":
    get_quotes()
