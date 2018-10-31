# os提供不少与操作系统相关的接口
import os

os.getcwd() #当前路径
os.system('mkdir today') #执行系统命令

# 针对日常的文件和目录管理任务，:mod:shutil 模块提供了一个易于使用的高级接口:

import shutil

shutil.copyfile(src, dst)
shutil.move(src, dst)


# glob模块提供了从通配符中搜索文件列表
import glob

glob.glob("*.py") #返回所有py文件
