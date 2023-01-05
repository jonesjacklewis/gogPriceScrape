import requests
from bs4 import BeautifulSoup
from typing import Union


def get_price_from_url(URL: str) -> Union[float, None]:
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, features="html.parser")

    PRICE_CLASS = "product-actions-price__final-amount"

    try:
        price = soup.find("span", {"class": PRICE_CLASS}).text
        return float(price)
    except AttributeError:
        return None

def main():
    URL = "https://www.gog.com/en/game/the_elder_scrolls_v_skyrim_anniversary_edition"

    if price := get_price_from_url(URL):
        print(price)
    else:
        print("Price not found")

if __name__ == '__main__':
    main()