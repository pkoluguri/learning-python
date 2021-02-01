import logging
import sys
import argparse
logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s:%(message)s",
    level=logging.DEBUG,
    datefmt="%I:%M:%S",
    stream=sys.stdout
)
logger = logging.getLogger("odd number generator")
class odd_number_generator():
    def __init__(self,number):
        self.number = number + 1
    def generate_odd_number(self):
     while self.number %2 == 0:
         self.number += 1
     yield self.number 
if __name__ == "__main__":
   parser = argparse.ArgumentParser(description="takes the starting number")
   parser.add_argument("-n","--starting_number",default=0,type=int,dest="starting_number")
   args = parser.parse_args()
   number = args.starting_number
   while True:
    ong = odd_number_generator(number)
    number = next(ong.generate_odd_number())
    logger.info("odd number:{}".format(number))
    logger.info("press enter to continue...")
    input()
