import time
from concurrent.futures import ProcessPoolExecutor

from utils import get_execute_time
from service import parse_smartphones
from service import parse_smartphone_urls
from config import BASE_URL




def main() -> None:
    """
    Function to execute the main logic of the program.
    This function utilizes multiprocessing to speed up the processing of smartphone data.
    """
    start_time = time.time()
    
    urls = parse_smartphone_urls(BASE_URL)

    end_time = time.time()
    minutes, seconds, milliseconds = get_execute_time(start_time, end_time)
    print(f"Execution time: {minutes}:{seconds}:{milliseconds}")

    start_time = time.time()
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(parse_smartphones, urls))

    end_time = time.time()
    minutes, seconds, milliseconds = get_execute_time(start_time, end_time)
    print(f"Execution time: {minutes}:{seconds}:{milliseconds}")

if __name__ == "__main__":
    main()
