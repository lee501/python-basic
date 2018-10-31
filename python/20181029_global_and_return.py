# 对着常规写法和global写法
def add(value1, value2):
  return value1 + value2

result = add(3, 5)

# 使用global
def add(value1, value2):
  global result
  result = value1 + value2

add(3, 5)
print(result)

# 返回多个return值
def profile():
  name = "lee"
  age = 30
  return name, age

