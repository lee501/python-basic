
'''
1, 通过网络共享文件，进入共享的文件目录下，然后在命令行运行以下代码
'''
python3 -m http.server

'''
2 漂亮的打印
'''
from pprint import pprint
a_dict = {'name': 'Yasoob', 'age': 'undefined', 'personality': 'awesome'}
pprint(a_dict)


'''
快速漂亮的从文件打印出json数据
'''
cat file.json | python -m json.tool

'''
脚本性能分析
'''
python -m cProfile my_script.py
 