# 函数缓存允许我们将给定参数的返回值缓存起来
# py3使用lru_cache装饰器
from functools import lru_cache
@lru_cache(maxsize=32)
def fib(n):
  if n < 2:
    return n
  return fib(n-1) + fib(n-2)
# 通过fib.cache_clear()清除缓存

# py2之前版本，自定义装饰

from functools import wraps

def memoize(func):
  memo = {}
  @wraps(func)
  def wrapper(*args):
    if args in memo:
      return memo[args]
    else:
      rv = func(*args)
      memo[args] = rv
      return rv
  return wrapper

@memoize
def fibo(n):
  if n < 2: return n
  return fibo(n-1)+fibo(n-2)
