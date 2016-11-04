#-*- coding:utf-8 -*-
#
import os
import requests
from pyquery import PyQuery as pq
url = 'http://jandan.net/ooxx'

headers = { "Accept":"text/html,application/xhtml+xml,application/xml;",
            "Accept-Encoding":"gzip",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Referer":"http://www.example.com/",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36"
            }
proxies = {
  "http": "http://183.61.236.55:3128",
  "https": "http://59.78.160.245:8080",
}

r = requests.get(url, headers=headers, proxies=proxies)

response = r.content
src_img = []
pq_content = pq(response).find('#comments').find('img')
for title in pq_content:
    # print pq(title).attr('src')
    # print pq(title).text
    src_img.append(pq(title).attr('src'))
     
print src_img
# print type(pq_content)
# print r.text.encode('utf-8')
try:
    os.mkdir('E:\\jd_img')
    
except Exception as err:
    print "%s目录已存在" % (err)
os.chdir('E:\\jd_img')
img_name = ''
for img in src_img:
    if img == None:
        continue
    img_name = img.split('/')[-1]
    print img_name
    img_res = requests.get(img, stream=True)
    with open(img_name, 'wb') as f:
        f.write(img_res.content)









