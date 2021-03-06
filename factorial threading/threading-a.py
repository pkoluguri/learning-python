import threading

def caluculate_factorial(number:int)->int:
 number_2 = number-1
 while number_2 > 0:
     number *= number_2
     number_2-=1 

if __name__ == "__main__":
 for i in range(1,1000):
     thread = threading.Thread(target=caluculate_factorial,args=[i,])
     print(i)
     thread.start()
