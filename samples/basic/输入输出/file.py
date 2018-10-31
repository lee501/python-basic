# 基于字符read & write
file = open('test.rb', w)
file.write ( 'This is a test.\nReally, it is.')
# 文件需要关闭
file.close()

# 读取整个文件并显示其中的数据。
file = open("test.rb")
print(file.read())
file.close()

# 读取一行
file.readline()

# 读取所有行，返回list
file.readlines()

'''
# 使用struct模块对二进制进行支持
# 转换成python 数据类型， 返回的是元组
'''
import struct
a = 13
bytes = struct.pack('i', a)

# 转换成python 数据类型， 返回的是元组
a = struct.unpack('i', bytes) 

'''
python中对文件、文件夹（文件操作函数）的操作需要涉及到os模块和shutil模块。
'''
# 分离路径和文件名
os.path.split('/home/swaroop/byte/code/poem.txt')
# 获取文件名
os.path.basename('/home/swaroop/byte/code/poem.txt')
# 获取路径名
os.path.dirname()

# 读取和设置环境变量:
os.getenv() 
os.putenv()

# 重命名：
os.rename（old， new）

# 创建多级目录：
os.makedirs（r“c：\python\test”）

# 创建单个目录：
os.mkdir（“test”）

# 获取文件属性：
os.stat（file）

# 修改文件权限与时间戳：
os.chmod（file）

# 终止当前进程：
os.exit（）

# 获取文件大小：
os.path.getsize（filename）

'''
目录操作：
os.mkdir("file") 创建目录
复制文件：
shutil.copyfile("oldfile","newfile") oldfile和newfile都只能是文件
shutil.copy("oldfile","newfile") oldfile只能是文件夹，newfile可以是文件，也可以是目标目录
复制文件夹：
shutil.copytree("olddir","newdir") olddir和newdir都只能是目录，且newdir必须不存在
重命名文件（目录）
os.rename("oldname","newname") 文件或目录都是使用这条命令
移动文件（目录）
shutil.move("oldpos","newpos") 
删除文件
os.remove("file")
删除目录
os.rmdir("dir")只能删除空目录
shutil.rmtree("dir") 空目录、有内容的目录都可以删
转换目录
os.chdir("path") 换路径

