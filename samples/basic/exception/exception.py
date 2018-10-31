# 自定义异常
class MyError(exception):
  def __init__(self, value):
    self.value = value

  def __str__(self): 
    return repr(self.value)

try:
  raise MyError(4)
except MyError as e:
  print("my error is value:", e.value)
