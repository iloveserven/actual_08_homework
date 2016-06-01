#!/bin/env python
# coding=utf-8
import sys
import requests
from pyquery import PyQuery as pq

reload(sys)
sys.setdefaultencoding('utf-8')

r = requests.get('https://www.douban.com/group/haixiuzu/')

for title in pq(r.content).find('.title')[:10]:
    url = pq(title).find('[href]').attr('href')
    subject = pq(title).text().encode('utf-8')
    # print url,subject
    r1 = requests.get(url)
    for img in pq(r1.content).find('.topic-figure'):
        src_url = pq(img).find('img').attr('src')
        pic_name = src_url.split('/')[-1]
        p = requests.get(src_url,verify=False)
        with open(pic_name,'w') as f:
            f.write(p.content)
        # print src_url,pic_name#,pq(p.content)