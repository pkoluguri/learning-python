import concurrent.futures

def caluculate_factorial(number:int,num_list:list)->tuple:
 number_2 = number-1
 while number_2 > 0:
     number *= number_2
     number_2-=1
 num_list.append(number)
 return (num_list,number)

if __name__ == "__main__":
  num_list_thread = []
  num_list_main = []
  with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
      for i in range(1,10):
          num_list_thread,num = executor.submit(caluculate_factorial,i,num_list_thread).result()
          num_list_main.append(num)