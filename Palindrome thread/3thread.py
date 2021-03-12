import io
import concurrent.futures
import time
import logging


format = "%(threadName)s : %(asctime)s: %(message)s"
logging.basicConfig(format=format, 
                    level=logging.INFO,
                    datefmt="%H:%M:%S")
logger = logging.getLogger("threads")

parsed_set = set()
source_list = []

def process(word):
    logger.info(f"got:{word}")
    reveresed_word = word[::-1]
    if reveresed_word == word:
        parsed_set.add(word)

if __name__ == "__main__":
    try:
     with io.open("words.txt",encoding="utf-8") as file:
        for word in file:
             word = word.replace("\n","").replace('"',"").replace(",","").replace("(","").replace(")","").replace(".","")
             if word != " " and word != "" and len(word) != 1:
              source_list.append(word)
    except FileNotFoundError:
        print("please run the writer.py file first!")
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:   
     s = time.perf_counter()
     executor.map(process,source_list)
     executor.shutdown(wait=True)
     e=time.perf_counter()-s
     print(parsed_set)
     print("took ",e,"seconds")
    