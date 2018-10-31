import random, time

# def stupid_fib(n):
#   index = 0
#   a = 0
#   b = 1
#   while index < n:
#     sleep_cnt = yield b
#     print (sleep_cnt) #4
#     print('let me think {0} secs'.format(sleep_cnt))  #5
#     time.sleep(sleep_cnt)
#     a, b = b, a + b
#     index += 1
# print('-'*10 + 'test yield send' + '-'*10) #1
# N = 20
# sfib = stupid_fib(N)
# print(sfib) #2
# fib_res = sfib.send(None)
# while True:
#   print(fib_res) #3
#   try:
#     fib_res = sfib.send(random.uniform(0, 0.5))
#   except StopIteration:
#     break
import asyncio
 
# Borrowed from http://curio.readthedocs.org/en/latest/tutorial.html.
@asyncio.coroutine
def countdown(number, n):
    while n > 0:
        print('T-minus', n, '({})'.format(number))
        yield from asyncio.sleep(1)
        n -= 1
 
loop = asyncio.get_event_loop()
tasks = [
    asyncio.ensure_future(countdown("A", 2)),
    asyncio.ensure_future(countdown("B", 3))]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
