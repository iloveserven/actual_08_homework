#-*-coding:utf-8-*-
import requests
from pyquery import PyQuery as pq 

r=requests.get('https://www.douban.com/group/haixiuzu/')
for title in pq(r.content).find('.title')[:10]:
	url=pq(title).find('[href]').attr('href')
	subject=pq(title).html().encode('utf-8')
	req=requests.get(url)
	for  img in pq(req.content).find('.topic-figure'):
              	src_url = pq(img).find('img').attr('src')
              	pic_name = src_url.split('/')[-1]
              	p= requests.get(src_url,verify=False)
              	with open(pic_name,'w') as f:
                                    f.write(p.content)
