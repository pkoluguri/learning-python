import logging
import sys
logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.DEBUG,
    datefmt="%I:%M:%S",
    stream=sys.stdout,
)
logger = logging.getLogger("generator")
previous_number = 1
number = 0
class fibonaci_generator():
 def __init__(self,previous_number,number):
     self.previous_number = previous_number
     self.number = number
 def next_fibonaci_number(self):
    yield self.previous_number + self.number
while True:
    logger.info("fibonaci number: {}".format(number))
    logger.info("press enter to continue...")
    input()
    fb = fibonaci_generator(previous_number,number)
    result = fb.next_fibonaci_number()
    previous_number = number
    number = next(result)