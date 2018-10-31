# 处理从 urls 接收的数据的 urllib.request 以及用于发送电子邮件的 smtplib

from urllib.request import urlopen

for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
  line = line.decode('utf-8')
  if 'love' in line or 'romatic' in line:
    print(line)

# 邮件
import smtplib

server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
..."""to: jcaesar@example.org
...from: soothsayer@example.org
... 
...baresasdada
...""")
server.quit()

# 处理get请求，不传data，则为get请求
import urllib
from urllib.request import urlopen
from urllib.request import urlencode

url='http://www.xxx.com/login'
data={"username":"admin","password":123456}
req_data=urlencode(data) #将字典类型的请求数据转变为url编码
res=urlopen(url+'?'+req_data)#通过urlopen方法访问拼接好的url
#read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str
res=res.read().decode()

#处理post请求,如果传了data，则为post请求
url='http://www.xxx.com/login'
data={"username":"admin","password":123456}
data = urlencode(data)
data=data.encode('ascii')#将url编码类型的请求数据转变为bytes类型
req_data=Request(url,data)#将url和请求数据处理为一个Request对象，供urlopen调用

#read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str
with urlopen(req_data) as res:
    res=res.read().decode()


