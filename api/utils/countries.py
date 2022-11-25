import collections
import re

import requests
from bs4 import BeautifulSoup

def get_countries():
    url = "https://www.worldometers.info/geography/alphabetical-list-of-countries/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(name="table")
    rows = results.find_all("tr", class_="")
    collected_countries = list()

    for row in rows:
        country = row.find_all("td", class_="")
        for index, value in enumerate(country):
            if index == 1:
                collected_countries.append(value.get_text())

    """ for country in collected_countries:
            print(type(country), country) """

    return collected_countries

print(get_countries())