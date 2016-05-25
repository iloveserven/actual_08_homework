#!/usr/bin/env python
# coding=utf-8

file_date={}

def update_data():
	with open('./user.txt') as f:
		for line in f:
			if not line:
				continue
			tmp = line.split(':')
			if len(tmp)==2:
				file_date[tmp[0]] = tmp[1].replace('\n','')

def update_file():
	user_list = []
	for user,pwd in file_date.items():
		user_list.append('%s:%s'%(user,pwd))
	with open('user.txt','w') as f:
		f.write('\n',join(user_list))

