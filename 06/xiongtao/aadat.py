file_data ={}

def update_data():
        with open('userss.txt') as f:
                for line in f:
                        if not line:
                                continue
                        tmp=line.split(':')
                        if len(tmp)==2:
                                file_data[tmp[0]]=tmp[1].replace('\n','')
def update_file():
        user_list=[]
        for user,passwd in file_data.items():
                user_list.append('%s:%s'%(user,passwd))
        print user_list
        with open('userss.txt','w') as f:
                f.write('\n'.join(user_list))
