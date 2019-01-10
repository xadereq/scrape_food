#!/usr/bin/python3

from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from pathlib import Path

BASE_URL = "https://www.maczfit.pl/menu/"


class Maczfit:
    def __init__(self):
        self.base_url = BASE_URL
        self.content = self.get_content()
        self.menu = self.get_menu()
        self.days = {}
        self.dinners = []
        self.get_days()
        self.get_dinners()
        self.print_dinners()

    @staticmethod
    def get_content(diet_type="fit"):
        full_url = urljoin(BASE_URL, diet_type)
        data = requests.get(full_url)
        return data.content

    @staticmethod
    def drop_whitespaces(string):
        while '  ' in string:
            string = string.replace('  ', ' ')
        return string.strip()

    @staticmethod
    def get_menu():
        # soup = BeautifulSoup(get_content(), 'html.parser')
        soup = BeautifulSoup(Path("test.html").read_text(), 'html.parser')
        table = soup.select("#content > div.section.woocommerce.menu-pane > div > div > div.menu > table > tbody")
        menu = table[0].find_all(recursive=False)
        return menu

    def get_days(self):
        for index, item in enumerate(self.menu, start=1):
            day = item.find_all("td", class_="label", limit=1)
            for date in day:
                date = self.drop_whitespaces(date.text)
                self.days[index] = date
        pass

    def get_dinners(self):
        for index, item in enumerate(self.menu, start=1):
            dinners = item.select("tbody > tr")
            dinners.pop()
            for dinner in dinners:
                dinner = dinner.find_all("td", class_="value")
                for food in dinner:
                    food = self.drop_whitespaces(food.text)
                    print(index)
                    print(food)
                    print(type(food))
            print("NEXT DAY ==================")

    def print_dinners(self):
        return print(self.dinners)


test = Maczfit()
