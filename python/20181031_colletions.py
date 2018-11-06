# python容器模块collections

#defaultdict
from collections import defaultdict

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

dfdict = defaultdict(list)
for name, colour in colours:
  dfdict[name].append(colour)

print(dfdict)
# defaultdict(<type 'list'>,
#    {'Arham': ['Green'],
#     'Yasoob': ['Yellow', 'Red'],
#     'Ahmed': ['Silver'],
#     'Ali': ['Blue', 'Black']
# })

# Counter
# 计数器
from collections import Counter

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favs = Counter(name for name, colour in colours)

favs #=> Counter({'Yasoob': 2, 'Ali': 2, 'Arham': 1, 'Ahmed': 1})


# deque 提供一个双端队列
from collections import deque

d = deque()
d.append(1)



