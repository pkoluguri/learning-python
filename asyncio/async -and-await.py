import asyncio
import random
import logging
import sys

logging.basicConfig(
    format ="%(asctime)s %(levelname)s:%(name)s:%(message)s",
    level=logging.DEBUG,
    datefmt="%I:%M:%S",
    stream=sys.stdout,
)
logger = logging.getLogger("async and await")
# the colors tupule
c = (
  "\033[0m",#white
  "\033[36m",#blue
  "\033[91m",#red
  "\033[35m"#purple
)
logger.info
                               
async def makerandom(idx:int,threshhold:int=6) -> int:
    #logger.infoing that the function has started
    logger.info(c[idx+1] + f"Initiated makerandom({idx+1})")
    #taking an random number 
    i = random.randint(0,10)
    #continuing the code below until the number is smaller than threshhold
    while i <= threshhold:
        #logger.infoing that the random number is too low  
        logger.info(c[idx+1]+f"makerandom({idx+1}) == {i} too low trying again")
        #sleeping for some time
        await asyncio.sleep(idx+1)
        #choosing another random number
        i =random.randint(0,10)
    #if the number was greater than the threshhold we are logger.infoing that the function has finished
    logger.info(c[idx+1] + f"---> finished: makerandom({idx+1}) == {i}" + c[0])
    #then we are returning the random number
    return i
async def main():
    #calling the makerandom function 3 times and getting the random number
    # the *() acts like next() it is used to hash an list
    res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(3)))
    #and returning the random number
    return res
if __name__ =="__main__":
 #calling the main function and getting the three random numbers r1,r2,r2
 r1,r2,r3 = asyncio.run(main())
 print()
 #logger.infoing the three random numbers
 logger.info(f"r1:{r1},r2:{r2},r3:{r3}")