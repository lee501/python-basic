# *args传递一个非键值对的可变数量的参数列表给函数

def test_args(first, *args):
  print("第一个参数是:{0}".format(first))
  for arg in args:
    print("其他参数来自*args:{0}".format(arg))

test_args('first', 'second', 'test')

# **kwargs 将不定长度的健值对作为参数传递给一个函数，函数中处理带名字的参数

def test_kwargs(**kwargs):
  for key, value in kwargs.items():
    print("{0}={1}".format(key, value))

test_kwargs(name="lee", sex="man")

# 使用*args和**kwargs 给函数传递参数
def test_args_kwargs(arg1, arg2, arg3):
  print("arg1:", arg1)
  print("arg2:", arg2)
  print("arg3:", arg3)

args = ("two", 2, 3)
test_args_kwargs(*args)

kwargs = {"arg3": 5, "arg2": "two", "arg1": 3}
test_args_kwargs(**kwargs)

# 参数的使用顺序
some_func(fargs, *args, **kwargs)
