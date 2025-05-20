# practice file for scraping book data. no pagination

import requests
from bs4 import BeautifulSoup
import csv

def scrape_books(url="https://books.toscrape.com/"):
    response = requests.get(url) # get response object
    response.raise_for_status() # raise error if request fails

    soup = BeautifulSoup(response.text, "html.parser") # create bs4 object

    # find all article class objects in the html doc
    books = soup.find_all("article", class_="product_pod")

    # set up the csv writer to write to books.csv
    with open("books.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price", "Availability"]) # write first row

        # loop through soup object and save important data
        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text[1:]
            in_stock = book.find("p", class_="instock availability").get_text(strip=True)

            writer.writerow([title, price, in_stock]) # write each row with the csv writer

if __name__ == "__main__":
    scrape_books()