import asyncio
import random

# the colors dictionary
c = (
  "\033[0m",#white
  "\033[36m",#blue
  "\033[91m",#red
  "\033[35m"#purple
)

                               
async def makerandom(idx:int,threshhold:int=6) -> int:
    #printing that the function has started
    print(c[idx+1] + f"Initiated makerandom({idx+1})")
    #taking an random number 
    i = random.randint(0,10)
    #continuing the code below until the number is smaller than threshhold
    while i <= threshhold:
        #printing that the random number is too low  
        print(c[idx+1]+f"makerandom({idx+1}) == {i} too low trying again")
        #sleeping for some time
        await asyncio.sleep(idx+1)
        #choosing another random number
        i =random.randint(0,10)
    #if the number was greater than the threshhold we are printing that the function has finished
    print(c[idx+1] + f"---> finished: makerandom({idx+1}) == {i}" + c[0])
    #then we are returning the random number
    return i
async def main():
    #calling the makerandom function 3 times and getting the random number
    res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(3)))
    #and returning the random number
    return res
if __name__ =="__main__":
 #calling the main function and getting the three random numbers r1,r2,r2
 r1,r2,r3 = asyncio.run(main())
 print()
 #printing the three random numbers
 print(f"r1:{r1},r2:{r2},r3:{r3}")