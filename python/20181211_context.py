# 实现上下文管理器的类，定义__enter__和__exit__方法
class File(object):
  def __init__(self, file_name, method):
    self.file_obj = open(file_name, method)

  def __enter__(self):
    return self.file_obj
  # __exit__三个参数是必须的, 用来处理异常
  def __exit__(self, type, value, traceback):
    self.file_obj.close()

with File('test.txt', 'w') as file:
  file.write("Hello Python")
'''
底层执行的顺序
1. with语句暂缓了File类的__exit__方法
2. 调用File类的__enter__方法
3. __enter__方法打开文件并返回给with语句
4. 传递给file参数
5. 使用write方法来写文件
6. with语句调用之前暂缓的__exit__方法
7. exit关闭文件
'''
# 异常的处理
'''
将type, value, traceback 传给exit来处理异常
1. 异常在__exit__中被优雅的处理，__exit__返回True， with不会处理异常
2. exit返回True以外的东西，这个异常会被with抛出
'''

# 在__exit__中处理异常

 def __exit__(self, type, value, traceback):
  print("处理异常")
  self.file_obj.close()
  return True



# 基于生成器的实现
from contextlib import contextmanager

@contextmanager
def open_file(name):
  f = open(name, 'w')
  yield f
  f.close()


































