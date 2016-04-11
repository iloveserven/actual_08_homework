#coding:utf-8

def opra(str):
        while True:
                op_list = []
                nu_list = []
                strr = ''
                str = raw_input("请输入你的运算(加减乘除),quit退出:")
		if str == '':
			continue
		if str == 'quit':
			break
                str_list = list(str)
                for i in str_list:
                        if i not in '+-*/':
                                strr += i
                        else:
                                nu_list.append(strr)
                                op_list.append(i)
                                strr = ''
                nu_list.append(strr)
                result = int(nu_list[0])
                for i in range(len(op_list)):
                        if  op_list[i] == '+':
                                result +=  int(nu_list[i+1])
                        if op_list[i] == '-':
                                result *=   int(nu_list[i+1])
                        if op_list[i] == '*':
                                result *=  int(nu_list[i+1])
                        if op_list[i] == '/':
                                try:
                                        result /=  int(nu_list[i+1])
                                except ZeroDivisionError as e:
                                        print "被除数不能为0"
#因为return会退出循环，此处采用print输出结果
	        print result
if __name__ == "__main__":
        print "计算结果为%s" % opra('')

