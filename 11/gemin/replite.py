#encoding: utf-8

import os
import requests
from pyquery import PyQuery as pq
#import re

def replite(url):
    img_path = '/srv/img/'
    if not os.path.exists(img_path):
        os.mkdir(img_path)
    r = requests.get(url)
    for page in pq(r.content).find('.olt').find('.title').find('a')[0:9]:
        url_sub = pq(page).attr('href')
        #print url_sub
        r_c = requests.get(url_sub)
        for img_url in pq(r_c.content).find('#link-report').find('img'):
            img_name = pq(img_url).attr('src').split('/')[-1]
            img = requests.get(pq(img_url).attr('src'))
            #print img
            with open(img_path + img_name,'w') as f:
                f.write(img.content)



if __name__ == "__main__":
    replite('https://www.douban.com/group/haixiuzu')
    #replite('http://neihanshequ.com')
