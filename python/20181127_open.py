# open的正确使用方法
with open("文件名", "r") as f:
  data = f.read()

'''
r只读
r+读取并写入
w覆盖写入文件
a文件末尾追加内容
'''

# 检查一个读取的文件类型
import io

with open('test.jpg', 'rb') as f:
  jdata = f.read()

if jdata.startswith(b'\xff\xd8'):
  text = u'This is a JPEG file (%d bytes long)\n'
else:
  text = u'This is a random file (%d bytes long)\n'


with io.open("text", 'w', encoding="utf-8") as outf:
  outf.write(text % len(jdata))
