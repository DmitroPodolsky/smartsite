import requests
from bs4 import BeautifulSoup

from utils import get_name
from utils import get_photo_url
from utils import get_price
from utils import get_characteristics

def parse_smartphone_urls(base_url: str) -> list[str]:
    """
    Function to parse smartphone URLs from the given base URL.
    
    Args:
        base_url: The base URL to start parsing smartphone URLs from.
    """
    urls = []
    
    for page_number in range(1, 6):
        url = base_url.format(page_number)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')

        # Находим все элементы <a> с указанным классом
        links = soup.find_all("a", class_="cup df full-height dib MainProductCard-module__link___35-Hg")

        # Перебираем все найденные элементы и извлекаем значение атрибута href
        for link in links:
            href = link.get('href')
            # Добавляем домен к значению атрибута href
            full_url = 'https://www.ctrs.com.ua' + href
            urls.append(full_url)
        
    return urls

def parse_smartphones(url: str) -> None:
    """
    Function to parse smartphone information from the given URLs.
    
    Args:
        url: URL to parse smartphone information from.
    """

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    name = get_name(soup)
    photo_urls = get_photo_url(soup)[:4]
    price = get_price(soup)
    characteristics = get_characteristics(soup)

    try:
        brand = characteristics["Основне"]["Серія"]
        diagonal = characteristics["Екран"]["Діагональ екрану"]        
        refresh_rate = characteristics["Екран"]["Частота оновлення екрану"]
        cores_number = characteristics["Процесор"]["Кількість ядер"]
        build_in_memory = characteristics["Пам'ять"]["Внутрішня пам'ять"]
        ram = characteristics["Пам'ять"]["Оперативна пам'ять"]
    except:
        pass
    else:        
        smartphone = [
            name,
            photo_urls,
            price,
            brand,
            diagonal,
            refresh_rate,
            cores_number,
            build_in_memory,
            ram
        ]

        print(smartphone)


