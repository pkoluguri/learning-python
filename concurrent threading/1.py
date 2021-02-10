import concurrent.futures
import logging 
import time

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
logger = logging.getLogger("threading")
logger1 = logging.getLogger("normal way")

def hello(num):
  print(num)
  time.sleep(1)

#0.4 secs
if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        start = time.perf_counter()
        executor.map(hello, range(3))
        end = time.perf_counter() - start
        logger.info(f"threading took:{end} second(s)")
        #3 secs
        start = time.perf_counter()
        hello(1)
        hello(2)
        hello(3)
        end = time.perf_counter() - start
        logger1.info(f"normal way took:{end} second(s)")