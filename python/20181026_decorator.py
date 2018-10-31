# 函数作为参数传递给另一个函数
def hi():
  return "hello girle"

def do_before_hi(funce):
  print("this is function do before hi")
  print(func())

do_before_hi(hi)

# 装饰器就是将函数作为参数，传递给内部函数（内部函数属于闭包的概念）
# 编写装饰器 decorator
def my_decorator(func):
  def wrapFunc():
    print("函数前输出信息")
    func()
    print("函数后输出信息")
  return wrapFunc

def test_func():
  print("内部的函数")

my_decorator(test_func)

# 装饰器封装一个函数
@my_decorator
def another_func():
  print("装饰器使用@")

another_func.__name__ #wrapFunc

# 让装饰器的名字返回为自身函数名字，使用functools.wraps
from functools import wraps

def a_new_decorator(a_func):
  @wraps(a_func)
  def wrapThisFunc():
    print("在函数参数调用之前输出")
    a_func()
    print("在函数参数调用之后输出")
  return wrapThisFunc

@a_new_decorator
def func_param():
  print("这是一个要传递的函数")


# 装饰器常用的场景，蓝本规范
from functools import wraps

def decorator_name(f):
  @wraps(f)
  def decoratored(*args, **kwargs):
    if not can_run:
      return "function will not run"
    return f(*args, **kwargs)
  return decoratored

@decorator_name
def func():
  return "function is running"

can_run = True
func() #function is running

can_run = False
func() #function will not run

# 基于装饰器的授权Authorization
from functools import wraps

def require_auth(f):
  @warps(f)
  def decoratored(*args, **kwargs):
    auth = request.authorization
    if not auth or not check_auth(auth.name, auth.password)
      authenticate()
    return f(*agrs, **kwargs)
  return decoratored


# 装饰器运用在日志logging上
from functools import wraps
def logit(f):
  @wraps(f)
  def with_logging(*args, **kwargs):
    print(f.__name__ + " was called")
    return f(*args, **kwargs)
  return with_logging

@logit
def addition_func(x):
  """do some math"""
  return x + x

# 包裹装饰器的函数，指定参数
from functools import wraps
def logit(logfile='out.log'):
  def logging_decorator(func):
    @wraps(func)
    def wrapped_function(*args, **kwargs):
      log_info = func.__name__ + " was called"
      print(log_info)
      with open(logfile, 'a') as file:
        file.write(log_info)
      return func(*args, **kwargs)
    return wrapped_function
  return logging_decorator

@logit()
def my_func():
  pass







































