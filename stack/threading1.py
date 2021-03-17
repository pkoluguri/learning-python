import time
import concurrent.futures
import threading

class stack():
    def __init__(self,maxsize=5,top=-1):
        self.maxsize = maxsize
        self.top = top
        self.stack_list = []
        self.lock = threading.Lock()

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
          with self.lock:  
           local_top = self.top
           local_top+=1
           time.sleep(0.1)
           self.top = local_top
          print(f"adding element {self.top}")
          self.stack_list.append(data)
        else:
            print(f"can't push {data} as the stack is full")
    
    def pop(self):
        if not self.is_empty():
         with self.lock:
            print(f"accesing element {self.top}")
            data = self.stack_list[self.top]
            local_top = self.top
            local_top-=1
            time.sleep(0.1)
            self.top = local_top
         return data 
        else:
            print("could not pop as the stack is empty")

if __name__ == "__main__":
    stack = stack()
    iterators = [1,2,3,4,5]
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
      executor.map(stack.push,iterators)
      time.sleep(1)
      executor.shutdown(wait=True)
    print(stack.stack_list)
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
      for _ in range(5): 
       result = executor.submit(stack.pop)
       results.append(result)
      executor.shutdown(wait=True)
    for result in results:
        print(result.result())
    print(stack.top)