#!/usr/bin/python
def app(str):
#����ȡ��str��ֳ�����list��һ�������ֵ����һ����������
        tmp_lst = list(str)
        num_lst = []
        num_str = ''
        code_lst = []
        for i in tmp_lst:
                if i not in ['+','-','*','/']:
                        num_str += i
                else:
                        num_lst.append(num_str)
                        code_lst.append(i)
                        num_str = ''
        num_lst.append(num_str)
#������������list��������
        res = int(num_lst[0])
        for i in range(len(code_lst)):
                if code_lst[i] == '+':
                        res += int(num_lst[i+1])
                elif code_lst[i] == '-':
                        res -= int(num_lst[i+1])
                elif code_lst[i] == '*':
                        res *= int(num_lst[i+1])
                else:
                        res /= int(num_lst[i+1])
        return res

input_str = raw_input('Please input your str: ')
print '%s == %s '%(input_str,app(input_str))
