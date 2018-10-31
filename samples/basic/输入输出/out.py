# str.format用法, 可变参数
print("{}网站: '{}!'".format("菜鸟网站", "www.zhihu.com"))

# 关键字参数
print("{name}网站： '{site}!'".format(name="菜鸟", site="zhihu.com"))

# 在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}

for name, number in table.items():
  print("{0: 10} ===> {1: 10}".format(name, number)
Runoob     ==>          2
Taobao     ==>          3
Google     ==>          1

# 旧的格式化%
print('常量 PI 的值近似为：%5.3f。' % math.pi)
