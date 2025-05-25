# practice quotes scraper

import requests
from bs4 import BeautifulSoup
import csv

class QuoteCrawler:
    # constructor
    def __init__(self):
        self.url = "http://quotes.toscrape.com/page/"
        self.page_number = 1

    # function to cycle through pages and print them all out
    def get_quotes(self):
        # continues to loop until the guard clause stops the loop when quotes aren't found on a page
        while True:
            response = requests.get(f"{self.url}{self.page_number}") # main url plus page number
            response.raise_for_status() # raises error if issue getting response

            soup = BeautifulSoup(response.text, "html.parser")

            quotes = soup.select(".quote")

            if not quotes: # guard clause to stop loop when no quotes are found
                print(f"No quotes found for page {self.page_number}")
                return

            # Finds all required info and writes to quotes.csv file in append mode
            # !!! Make sure quotes.csv is empty prior to each run !!!
            with open('quotes.csv', 'a', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile, quotechar='"', quoting=csv.QUOTE_ALL)
                for quote_div in quotes: # loops through each quote on the page
                    quote = quote_div.find("span", class_="text").text.strip() # get the quote
                    quote = self.clean_quotes(quote) # Remove all quotes from test
                    author = quote_div.find("small", class_="author").text # get the author's name
                    tags = quote_div.find_all("a", class_="tag") # get any associated tags
                    tag_list = [tag.text.strip() for tag in tags] # list comprehension to create a list of tags for each quote
                    tag_str = ", ".join(tag_list) # join the tag_list as a string to help with csv writing cleanly

                    # writes each row to quotes.csv
                    writer.writerow([quote, author, tag_str])

            print(self.page_number) # print page number for debugging
            self.page_number += 1 # increment page number after each page is scraped

    # function used to remove quotes from all scraped text
    def clean_quotes(self, raw_quote: str) -> str:
        return raw_quote.replace("“", '').replace("”", '').replace("‘", "").replace("’", "")


if __name__ == "__main__":
    # open quotes.csv, clear it, and write a header
    with open('quotes.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL) # create new writer
        writer.writerow(["Quote", "Author", "Tags"]) # write header

    crawler = QuoteCrawler() # create QuoteCrawler object
    crawler.get_quotes() # scrape the url
