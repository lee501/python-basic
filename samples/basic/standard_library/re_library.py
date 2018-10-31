# re模块为高级字符串处理提供了正则表达式工具

import re

# match()方法是从字符串的开头开始匹配，一旦开头不匹配，那么整个匹配就失败了

print(re.match(r'\Bf[a-z]*', "which foot or hand fell fastest"))

print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配

print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配

# 切分字符串
#   使用正则切分
re.split(r'[\s\,\;]+', 'a,b;; c  d')

#  字符串自带
'a b   c'.split(' ')

# search()，它在匹配时会扫描整个字符串，然后返回第一个成功匹配的结果
print(re.search(r'\bf[a-z]*', "which foot or hand fell fastest"))
# >><_sre.SRE_Match object; span=(6, 10), match='foot'>