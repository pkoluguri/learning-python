import asyncio
import random
import time

async def part1(n: int) -> str:
    i = random.randint(0,10)
    print(f"part1({n}) sleeping for {i} seconds.")
    #sleeping for random time
    await asyncio.sleep(i)
    result = f"result {n}-1"
    print(f"returning part 1({n}) == {result}.")
    return result
async def part2(n: int, arg:str) -> str:
    i=random.randint(0,10)
    print(f"part2{n, arg} sleeping for {i} seconds.")
    #sleeping for random time
    await asyncio.sleep(i)
    result = f"result{n}-2 derived from {arg}"
    print(f"returning part2{n,arg} == {result}.")
    return result

async def chain(n: int) -> None:
    #starting the timer
    start = time.perf_counter()
    #calling part1 with await keyword
    p1 = await part1(n)
    #calling part2 with awaitk keyword
    p2 = await part2(n,p1)
    #ending the timer
    end = time.perf_counter() -start
    #printing how long it took
    print(f" -->Chained result{n} => {p2} (took {end:0.2f} seconds).")

#the main function
async def main(*args):
    #running the chain function for the args given 
    await asyncio.gather(*(chain(n) for n in args))

if __name__ == "__main__":
    import sys
    #defaulting to args to 1,2,3 if any args for not given if any args were given converting them to intigers from strings
    args = [1,2,3] if len(sys.argv) == 1 else map(int,sys.argv[1:])
    #starting the timer
    start = time.perf_counter()
    #running the main function
    asyncio.run(main(*args))
    #ending the timer
    end = time.perf_counter() - start
    #printing the time taken
    print(f"Program finished in {end:0.2f} seconds")