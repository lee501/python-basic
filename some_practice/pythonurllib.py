from urllib import request

# urllib的request模块可以非常方便地抓取URL内容
req = request.Request('https://passport.weibo.cn/sso/login')
with request.urlopen(req) as f:
  data = f.read()
  print('Status:', f.status, f.reason)
  for k, v in f.getheaders():
    print('%s: %s' % (k, v))
  print('Data:', data.decode('utf-8'))  

# 代理
proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    pass  