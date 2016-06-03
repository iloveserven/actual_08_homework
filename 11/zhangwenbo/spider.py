
# enconding=utf-8
import requests
from pyquery import PyQuery as py

R = requests.get('https://www.douban.com/group/haixiuzu/')

for i in py(R.content).find('.title').find('[href]')[9:19]:
	url = requests.get(py(i).attr('href'))
	for c in py(url.content).find('#link-report').find('[src]'):
		uc = py(c).attr('src')
		image_name = uc.split('/')[-1]
		img = requests.get(uc)
		with open(image_name,'w') as f:
			f.write(img.content)







