# 字典dict{key: value}, key是不可变对象，通常是数字和字符串

tel = { 'jack': 4098, 'sape': 4139 }

# keys方法
tel.keys() #>>>dict keys (['jack', 'spae'])
list(tel.keys()) #['jack', 'spae']

# sorted
sorted(tel.keys())

# in 方法判断是否存在key
'jack' in tel #>>> true

# 使用dict构造，通过对 键值对元组列表[('space', 123),()] 构建字典
dict([('space', 123), ('lee', 456)])

# 使用复制方式，简单构造字典
dict(sape=4139, guido=4127, jack=4098)

# dict的遍历
# k，v值可以使用items直接解读出来
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
  print(k, v)

# list遍历
# 使用enumerate()获取索引和对应值
for i, v in enumerate([1,2,3]):
  print(i, v)
