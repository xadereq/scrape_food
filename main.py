#!/usr/bin/python3

from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from pathlib import Path

BASE_URL = "https://www.maczfit.pl/menu/"


class Menu:
    def __init__(self):
        self.base_url = BASE_URL
        self.content = self.get_content()

    def get_content(self, diet_type="fit"):
        full_url = urljoin(BASE_URL, diet_type)
        data = requests.get(full_url)
        return data.content

    def get_menu(self):
        # soup = BeautifulSoup(get_content(), 'html.parser')
        soup = BeautifulSoup(Path("/tmp/test.html").read_text(), 'html.parser')
        table = soup.select("#content > div.section.woocommerce.menu-pane > div > div > div.menu > table > tbody")
        menu = table[0].find_all(recursive=False)
        for days in menu:
            for day in days:
                print(day.string)
        return print("XD")


test = Menu()
test.get_menu()
