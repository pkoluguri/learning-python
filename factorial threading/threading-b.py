import concurrent.futures


def caluculate_factorial(number):
   number_2 = number-1
   while number_2 > 0:
     number *= number_2
     number_2-=1
   return number

if __name__ == "__main__":
 with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
  for i in range(1,1000):
    executor.submit(caluculate_factorial,i)
