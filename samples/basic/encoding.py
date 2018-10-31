# 计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码

# 记事本
用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，
编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件：

# 服务器时候
浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器：

# python3中： 字符串是以Unicode编码


# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：

len('ABC')
len(b'ABC')

len('中文') #>>2
len('中文'.encode('utf-8')) #>> 6