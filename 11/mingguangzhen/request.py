#encoding=utf-8
#
import requests
from pyquery import PyQuery as pq


# requests.post('http://localhost/add_user', data={'user':'testuser','pwd':'123'})
# 
# 

r = requests.get('https://www.douban.com/group/haixiuzu/')
url_r = pq(r.content).find('#group-topics').find('.title').find('a')
# print url_r
url_list = []
for one in url_r:
    #print pq(one).split('\"')[1]
    tmp_one = pq(one).attr('href')
    #print tmp_one.attr('href')
    url_list.append(tmp_one)
    #break
    #print pq(one).text().encode('utf-8')
#print url_list
img_src_list = [] 
#image_r = requests.get('https://www.douban.com/group/topic/87032888/')
for _src in url_list:
    img_r = requests.get(_src)
    img_src = pq(img_r.content).find('#link-report').find('img').attr('src')

    img_src_list.append(img_src)

print img_src_list
for img_url in img_src_list:
    if img_url == None:
        continue
    print img_url
    img_name = img_url.split('/')[-1]
#print img_name
    # response = requests.get(img_src, stream=True)
    response = requests.get(img_url, stream=True)
    with open(img_name,'wb') as f:
        f.write(response.content)

# pirnt img_file

#with open(img_name, 'w') as f:
#    f.write(pq(img_file.content))







# photo_read = pq(r.content).find('.text').find('img')
# print photo_read

    # print pq(title).text()
    # print pq(title).html()
    # print pq(title).html().encode('utf-8')
