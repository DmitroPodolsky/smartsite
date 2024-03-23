import asyncio
from concurrent.futures import ProcessPoolExecutor

import aiohttp
from bs4 import BeautifulSoup

from utils import fetch_html_from_url
from utils import get_name
from utils import get_photo_url
from utils import get_price
from utils import get_characteristics


async def parse_smartphone_urls(base_url: str) -> list[str]:
    """
    Extracts the HTML content of smartphone pages from the given base URL.

    Args:
        base_url: The base URL to extract smartphone page URLs from.
    """
    urls = []
    pages_url = base_url + '/smartfony/page_{}/'
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_html_from_url(session, pages_url.format(page_number)) for page_number in range(1, 6)]
        pages = await asyncio.gather(*tasks)
        
        for page in pages:
            soup = BeautifulSoup(page, 'html.parser')
            links = soup.find_all("a", class_="cup df full-height dib MainProductCard-module__link___35-Hg")
            for link in links:
                href = link.get('href')
                full_url = base_url + href
                urls.append(full_url)
        
        tasks = [fetch_html_from_url(session, url) for url in urls]
        htmls = await asyncio.gather(*tasks)
        
    return htmls

def parse_smartphone_sync(html: str) -> None:
    """
    Function to parse smartphone information from the given HTML.

    Args:
        html: HTML string representing the webpage to parse smartphone information from.
    """
    soup = BeautifulSoup(html, 'html.parser')

    name = get_name(soup)
    photo_urls = get_photo_url(soup)
    price = get_price(soup)
    characteristics = get_characteristics(soup)

    try:
        smartphone = [
            name,
            photo_urls,
            price,
            characteristics.series,
            characteristics.screen_diagonal,
            characteristics.screen_refresh_rate,
            characteristics.number_of_cores,
            characteristics.internal_memory,
            characteristics.ram
        ]
    except ValueError as e:
        print(f"ValueError: {e}")
    else:
        print(smartphone)


async def parse_smartphones_in_parallel(htmls: list[str]) -> None:
    """
    Parses smartphone information from multiple HTMLs in parallel using a process pool.

    Args:
        htmls: A list of HTML strings from which smartphone information will be parsed.
    """
    loop = asyncio.get_running_loop()

    with ProcessPoolExecutor() as pool:
        tasks = [loop.run_in_executor(pool, parse_smartphone_sync, html) for html in htmls]
        await asyncio.gather(*tasks)


