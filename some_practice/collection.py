# namedtuple
# namedtuple('名称', [属性list]):
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
p.x = 1
p.y = 2

# deque 实现双向list操作
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('d')
q.appendleft('A')

# defaultdict
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['a'] = 1
dd['b'] = 2

# OrderedDict 保持key顺序
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# OrderedDict可以实现一个FIFO（先进先出）的dict
# class LastUpdateOrderedDict(OrderedDict):
#   def __init__(self, capacity):
#     # super(LastUpdateOrderedDict, self).__init__()
#     super().__init__()
#     self.__capacity = capacity

#   def __setitem__(self, key, value):
#     containsKey = 1 if key in self else 0
#     if len(self)
ns = intertools.repeat('A', 3)
for n in ns:
    print(n)

#读取文件
try:
  f = open('/path/file', 'r')
  f.read()
finally:
  if f:
    f.close()  
# 使用with
with open('/path/to/file', 'r') as f:
  f.read() 

#实现上下文管理是通过__enter__和__exit__这两个方法实现的
class Query(object):
  def __init__(self, name):
    self.name = name

  def __enter__(self):
    print('begin')
    return self 

  def __exit__(self, exc_type, exc_value, traceback):
    if exc_type:
      print('error')
    else:
      print('end')

  def query(self):
    print('query info about %s...' % self.name)

             

























