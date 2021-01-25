import logging
import sys
logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s:%(message)s",
    level=logging.DEBUG,
    datefmt="%I:%M:%S",
    stream=sys.stdout
)
logger = logging.getLogger("odd number generator")
class odd_number_generator():
    def __init__(self,number):
        self.number = number
    def generate_odd_number(self):
     number_yeilded = False
     while not number_yeilded: 
      if self.number %2 != 0:
         number_yeilded = True
         yield self.number
      else:
          self.number+=1
while True:
   ong = odd_number_generator(number)
   number = next(ong.generate_odd_number())
   logger.info("odd number:{}".format(number))
   logger.info("press an key to continue...")
   input()
   number+=1