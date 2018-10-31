# 复写python专用方法的例子

# __str__
class People:
  
  def __init__(self, name, age):
    self.a = name
    self.b = age
    
  def __str__(self):
    return self.a

people = People('lee', 28)

