#httplib2返回的是字节串（bytes）, 需要decode
import httplib2
h = httplib2.Http('.cache')
response, content = h.request('uri')
response.status
content[:52]

# 处理Last_Modified和Etag
httplib2.debuglevel = 1
h = httplib2.Http('.cache')
response, content = h.request('http://uri')
connect: (diveintopython3.org, 80)
send: b'GET / HTTP/1.1
Host: diveintopython3.org
accept‐encoding: deflate, gzip
reply: 'HTTP/1.1 302 Found'
send: b'GET /examples/feed.xml HTTP/1.1

# 
form urllib.parse import urlencode
data = {'status': 'test python3'}
urlencode(data) #'status=test+python3'

h = httplib2.Http('.cache')
h.add_credentials('', 'psd', '')
resp, content = h.request('url', 'post', urlencode(data), headers={'Content‐Type': 'application/x‐www‐ form‐urlencoded'})

# 对content的处理
from xml.etree import ElementTree as etree
tree = etree.fromstring(content)
status_id = tree.findtext('id')
url = 'https://identi.ca/api/statuses/destroy/{0}.xml'.format(status_id)

resp, delete_content = h.request(url, 'DELETE')
