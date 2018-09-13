import asyncio
from random import randint


async def is_prime(x):
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                break
        else:
            print(str(x) + ' is prime')
            return x
    return 0


async def prime_sum(first, last):
    res = 0
    for i in range(first, last + 1):
        res += await is_prime(i)
    print(res)


if __name__ == '__main__':
    start = randint(1, 50)
    finish = randint(1, 50) + start + 1
    loop = asyncio.get_event_loop()
    loop.run_until_complete(prime_sum(start, finish))
    loop.close()
