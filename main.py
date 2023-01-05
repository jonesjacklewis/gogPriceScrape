import requests
from bs4 import BeautifulSoup
from typing import Union
import configparser

def get_url(config_file: str = "main.ini") -> str:
    config = configparser.ConfigParser()
    config.read(config_file)

    return config["gog_url"]["url"]

def get_price_from_url(url: str) -> Union[float, None]:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, features="html.parser")

    PRICE_CLASS = "product-actions-price__final-amount"

    try:
        price = soup.find("span", {"class": PRICE_CLASS}).text
        return float(price)
    except AttributeError:
        return None

def main():
    url = get_url()

    if price := get_price_from_url(url):
        print(price)
    else:
        print("Price not found")

if __name__ == '__main__':
    main()