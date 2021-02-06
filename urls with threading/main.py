import threading
import requests
import logging
import sys
import re

logging.basicConfig(
  format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
  level=logging.DEBUG,
  datefmt="%I:%M:%S",
  stream=sys.stdout,
)

logger = logging.getLogger("main")

re_href = re.compile(r'href="(.*?)"')

def fetch_html(url):
   html = requests.get(url)
   html.raise_for_status()
   return html.text

def parse(url):
    found = set()
    try:
      html = fetch_html(url)
    except(
        requests.ConnectionError,
        requests.ConnectTimeout,
    ) as e:
     logger.error(f"timeout error at {url}: {e}")
     return found
    except Exception as e:
      logger.exception(f"uknown exception at {url}: {e}")
      return found
    else:
        for link in re_href.findall(html):
            found.add(link)
    logger.info(f"Found {len(found)} links for {url}")
    return found

def write_one(file,url):
    urls = parse(url)
    if not urls:
        return None
    with open(file,"a") as f:
        for url1 in urls:
            f.write(f"{url}\t{url1}\n")
    logger.info(f"wrote results for {url}")

def bulk_crawl_and_write(file:str,urls:set)->None:
    for url in urls:
        write_one(file,url)

if __name__ == "__main__":
    import pathlib
    import sys
    assert sys.version_info >= (3,7)
    here = pathlib.Path(__file__).parent
    with open(here.joinpath("urls.txt")) as file:
        urls = set(map(str.strip,file))
    outpath = here.joinpath("foundurls.txt")
    with open(outpath,"w") as ofile:
        ofile.write("source_url\tparsed_url\n")
    thread = threading.Thread(target=bulk_crawl_and_write,args=(outpath,urls,))
    thread.start()