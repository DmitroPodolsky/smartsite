from bs4 import BeautifulSoup
from aiohttp import ClientSession

from models import SmartphoneCharacteristics


def get_photo_url(soup: BeautifulSoup) -> list[str]:
    """
    Extracts photo URLs from the BeautifulSoup object representing a webpage.

    Args:
        soup: The BeautifulSoup object representing the webpage.
    """
    photo = []
    picture_urls = soup.find_all("img", class_="ProductSlider-module__image___1qhoG")
    for picture_url in picture_urls[:4]:
        src = picture_url.get('src')
        photo.append(src)
    return photo
        

def get_name(soup: BeautifulSoup) -> str:
    """
    Extracts the name of the product from the BeautifulSoup object representing a webpage.

    Args:
        soup: The BeautifulSoup object representing the webpage.
    """
    title = soup.find("h1", class_="Description_title__dkBmI").get_text()
    return title


def get_price(soup: BeautifulSoup) -> int:
    """
    Extracts the price of the product from the BeautifulSoup object representing a webpage.

    Args:
        soup: The BeautifulSoup object representing the webpage.
    """
    price = soup.find("div", class_="price medium no-wrap f-secondary Price_price__KKCnw").get("data-price")
    return int(price)


def get_characteristics(soup: BeautifulSoup) -> SmartphoneCharacteristics:
    """
    Extracts the characteristics of the product from the BeautifulSoup object representing a webpage.

    Args:
        soup: The BeautifulSoup object representing the webpage.
    """
    characteristics_divs = soup.find_all("div", class_="Characteristic_characteristic__NGJor")
    smartphone_characteristics = SmartphoneCharacteristics()

    for div in characteristics_divs:
        category_data = {span.get_text(strip=True): p.get_text(strip=True) 
                        for span, p in zip(div.find_all('span'), div.find_all('p'))}
        
        for key, value in category_data.items():
            english_key = smartphone_characteristics.ukrainian_to_english.get(key)
            if english_key and english_key in smartphone_characteristics.__dict__:
                setattr(smartphone_characteristics, english_key, value)
            else:
                print(f"Warning: Unknown characteristic '{key}'")

    return smartphone_characteristics


def get_execute_time(start_time: float, end_time: float) -> None:
    """
    Calculates the execution time in minutes, seconds, and milliseconds.

    Args:
        start_time: The start time in seconds since the epoch.
        end_time: The end time in seconds since the epoch.
    """
    execution_time = end_time - start_time

    minutes = int(execution_time // 60)
    seconds = int(execution_time % 60)
    milliseconds = int((execution_time - int(execution_time)) * 1000)
    print(f"Execution time: {minutes}:{seconds}:{milliseconds}")


async def fetch_html_from_url(session: ClientSession, url: str) -> str:
    """
    Fetches HTML content from the specified URL asynchronously.

    Args:
        session: The aiohttp ClientSession object.
        url: The URL from which to fetch HTML content.
    """
    async with session.get(url) as response:
        return await response.text()