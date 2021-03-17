import logging
import time

logging.basicConfig(
    datefmt="%I:%M:%S",
    level=logging.DEBUG,
    format="%(threadName)s : %(asctime)s : %(message)s"
)

logger = logging.getLogger("Stack")


class stack():
    def __init__(self,maxsize=5,top=-1):
        self.maxsize = maxsize
        self.top = top
        self.stack_list = []

    def is_empty(self):
      if self.top == -1:
          return True
      else :
          return False
    
    def is_full(self):
        if self.top == self.maxsize:
            return True
        else:
            return False

    def push(self,data):
        if not self.is_full():
           local_top = self.top
           local_top+=1
           time.sleep(0.1)
           self.top = local_top
           logger.info(f"adding element {self.top}")
           self.stack_list.append(data)
        else:
            logger.error(f"can't push {data} as the stack is full")
    
    def pop(self):
        if not self.is_empty():
            logger.info(f"accesing element {self.top}")
            data = self.stack_list[self.top]
            local_top = self.top
            local_top-=1
            time.sleep(0.1)
            self.top = local_top
            return data 
        else:
            logger.error("could not pop as the stack is empty")
    
if __name__ == "__main__":    
 stack = stack()
 for i in range(1,6):
     stack.push(i)
 for _ in range(6):
     logger.info(f"got {stack.pop()}")
 print(stack.stack_list)