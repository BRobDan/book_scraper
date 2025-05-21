# practice scraper for remoteok.com job board

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

driver.get("https://remoteok.com/")
time.sleep(5)  # wait for JS to load jobs

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

jobs = soup.select("td.company.position.company_and_position")
print(f"Found {len(jobs)} jobs")

for job in jobs:
    title = job.find("h2", attrs={"itemprop": "title"})
    if title:
        print(title.text.strip())

driver.quit()

