#coding=utf-8
import requests
from pyquery import PyQuery as pq
import sys

r =requests.get(sys.argv[1])
for title in pq(r.content).find('.zm-item').find('.question_link'):
    print pq(title).html().encode('utf-8')
