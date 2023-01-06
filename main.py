import requests
from bs4 import BeautifulSoup
from typing import Union
import configparser
import smtplib
from email.mime.text import MIMEText

DEFAULT_CONFIG = "main.ini"

def get_url(config_file: str = DEFAULT_CONFIG) -> str:
    config = configparser.ConfigParser()
    config.read(config_file)

    return config["gog"]["url"]

def get_max_price(config_file: str = DEFAULT_CONFIG) -> Union[float, None]:
    config = configparser.ConfigParser()
    config.read(config_file)

    try:
        return float(config["gog"]["max_price"])
    except ValueError:
        return None

def get_email_password(config_file: str = DEFAULT_CONFIG) -> str:
    config = configparser.ConfigParser()
    config.read(config_file)

    return config["email"]["password"]

def get_from_email(config_file: str = DEFAULT_CONFIG) -> str:
    config = configparser.ConfigParser()
    config.read(config_file)

    return config["email"]["from"]

def get_email_host(config_file: str = DEFAULT_CONFIG) -> str:
    config = configparser.ConfigParser()
    config.read(config_file)

    return config["email"]["host"]

def get_email_to(config_file: str = DEFAULT_CONFIG) -> str:
    config = configparser.ConfigParser()
    config.read(config_file)

    return config["email"]["to"]

def get_soup_from_url(url: str) -> Union[BeautifulSoup, None]:
    try:
        r = requests.get(url)
        return BeautifulSoup(r.content, features="html.parser")
    except:
        return None

def get_title_from_soup(soup: BeautifulSoup) -> Union[str, None]:
    TITLE_CLASS = "productcard-basics__title"

    try:
        return soup.find("h1", {"class": TITLE_CLASS}).text
    except AttributeError:
        return None

def get_price_from_soup(soup: BeautifulSoup) -> Union[float, None]:
    PRICE_CLASS = "product-actions-price__final-amount"

    try:
        price = soup.find("span", {"class": PRICE_CLASS}).text
        return float(price)
    except AttributeError:
        return None
    
def send_email(username, password, service, subject, to, message):
    msg = MIMEText(message)

    msg['Subject'] = subject
    msg['From'] = username
    msg['To'] = to

    s = smtplib.SMTP_SSL(service)
    s.login(username, password)
    s.sendmail(username, to, msg.as_string())

def send_price_alert(title, price):
    password = get_email_password()
    from_email = get_from_email()
    host = get_email_host()
    to = get_email_to()

    subject = f"GOG price alert | {title}"
    message = f"{title} is now {price}"

    send_email(from_email, password, host, subject, to, message)

def main():
    url = get_url()

    if soup := get_soup_from_url(url):
        title = get_title_from_soup(soup)
        price = get_price_from_soup(soup)
        
        max_price = get_max_price()

        if not max_price:
            return

        if title and price and price <= max_price:
            send_price_alert(title, price)


if __name__ == '__main__':
    main()