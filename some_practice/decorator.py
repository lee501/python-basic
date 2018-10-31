import functools

# 装饰器
# now = log('execute')(now)
  # 第一步执行log('execute') => decorator函数
  # 第二部执行decorator(now) => wrapper
  # now = wrapper, now()
def log(text):
  def decorator(func):
    @functools.wraps(func) #指定__name__属性为函数名
    def wrapper(*args, **kw):
      print('%s %s():' % (text, func.__name__))
      return func(*args, **kw)
    return wrapper
  return decorator  

@log('execute')
def now():
  print('2018-2-7')

  #匿名函数 lambda x: x * x 
  lambda x: pass
