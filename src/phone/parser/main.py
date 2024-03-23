import asyncio
import time


from utils import get_execute_time
from service import parse_smartphones_in_parallel
from service import parse_smartphone_urls
from config import BASE_URL


async def main() -> None:
    """
    Function to execute the main logic of the program.
    This function utilizes multiprocessing to speed up the processing of smartphone data.
    """
    start_time = time.time()
    
    urls = await parse_smartphone_urls(BASE_URL)

    await parse_smartphones_in_parallel(urls)

    end_time = time.time()
    get_execute_time(start_time, end_time)


if __name__ == "__main__":
    asyncio.run(main())
