import asyncio
import logging
import re
import sys
from typing import IO
import urllib.error
import urllib.parse
import aiofiles
import aiohttp
from aiohttp import ClientSession

#setting the basic configuration of logging
logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.DEBUG,
    datefmt="%H:%M:%S",
    stream=sys.stdout,
)
#didn't understand this-v
logger = logging.getLogger("areq")
logging.getLogger("chardet.charsetprober").disabled = True
#-----------------------------------------
#making a pattern object of the pattern (href="(.*?)")
HREF_RE = re.compile(r'href="(.*?)"')

#this is the function to fetch the html of the website of an given url
async def fetch_html(url: str, session: ClientSession, **kwargs) -> str:
    #we are taking the url given and sending a request and getting a response
    resp = await session.request(method="GET", url=url, **kwargs)
    resp.raise_for_status()
    #we are sending a message to the console abot the status code from the url
    logger.debug("Got response [%s] for URL: %s", resp.status, url)
    #we are taking the html from the resp object and storing it in html variable
    html = await resp.text()
    #we are returning html variable
    return html

#this is the function to parse the html 
async def parse(url: str, session: ClientSession, **kwargs) -> set:
    #making an set for found urls
    found = set()
    try:
        #getting the html for the url given
        html = await fetch_html(url=url, session=session, **kwargs)
    #if there is an error in the url we are letting the user know there is an error in the given url 
    except (
        aiohttp.ClientError,
        aiohttp.http_exceptions.HttpProcessingError,
    ) as e:
        logger.error(
            "aiohttp exception for %s [%s]: %s",
            url,
            getattr(e, "status", None),
            getattr(e, "message", None),
        )
        return found
    #if there is an uknown error we are letting the user know that and returning an blank set found
    except Exception as e:
        logger.exception(
            "Non-aiohttp exception occured:  %s", getattr(e, "__dict__", {})
        )
        return found
    # if there is no error we are running the below code
    else:
        #we are using HREF_RE pattern to fing the links in html
        for link in HREF_RE.findall(html):
            try:
                #then we are parsing the url
                abslink = urllib.parse.urljoin(url, link)
            #if there is an error in parsing the url then we are letting the user know
            except (urllib.error.URLError, ValueError):
                logger.exception("Error parsing URL: %s", link)
                pass
            #if there is no error we are adding the parsed url to the found set
            else:
                found.add(abslink)
        # and then sending the message about how many links have been found
        logger.info("Found %d links for %s", len(found), url)
        # then returning the found set
        return found

#this is the function to write all the suburls for an given url
async def write_one(file: IO, url: str, **kwargs) -> None:
    #first we are getting the found set from the parse function and storing it in res 
    res = await parse(url=url, **kwargs)
    #if res is an empty set we are returning None
    if not res:
        return None
    #we are opening the given file in a mode     
    async with aiofiles.open(file, "a") as f:
        #and for evry suburl we are writing it to the file 
        for p in res:
            await f.write(f"{url}\t{p}\n")
        #we are sending an message that the program has written all the suburls of the url
        logger.info("Wrote results for source URL: %s", url)

#this function is to write all the suburls of evry url in the file to another file 
async def bulk_crawl_and_write(file: IO, urls: set, **kwargs) -> None:
    async with ClientSession() as session:
        tasks = []
        # for evry url we are making an session and adding it to the tasks list
        for url in urls:
            tasks.append(
                write_one(file=file, url=url, session=session, **kwargs)
            )
        #and we are running evry task in tasks
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    import pathlib
    import sys
    
    #to check that the version of python is above 3.7
    assert sys.version_info >= (3, 7) 
    #didn't understand this
    here = pathlib.Path(__file__).parent
    with open(here.joinpath("urls.txt")) as infile:
        urls = set(map(str.strip, infile))
    #we are making an file outpath
    outpath = here.joinpath("foundurls.txt")
    with open(outpath, "w") as outfile:
        #we are writing source_url and parsed_url
        outfile.write("source_url\tparsed_url\n")
    #then we are running the bulk_crawl_and_write function and giving urls to it and the outpath file
    asyncio.run(bulk_crawl_and_write(file=outpath, urls=urls))