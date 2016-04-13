#encoding=utf8
#
# 将要计算的字符串筛选出数字和符号并转换
def convert(_str = calc_str):
    _str = _str.replace('+',' + ')
    _str = _str.replace('-',' - ')
    _str = _str.replace('*',' * ')
    _str = _str.replace('/',' / ')
    return _str.split()
# 将取出的列表中的三个元素做运算
def calc(_list):
    #print _list
    if _list[1] == '+':
        return int(_list[0]) + int(_list[2])
    elif _list[1] == '-':
        return int(_list[0]) - int(_list[2])
    elif _list[1] == '*':
        return int(_list[0]) * int(_list[2])
    elif _list[1] == '/':
        return int(_list[0]) / int(_list[2])
# 取出列表前三个元素交给calc计算，递归出最后值
def recu(con_list):
    if len(con_list) <= 3:
        return calc(con_list)
    else:
        return recu([calc(con_list[0:3])]+con_list[3:])

calc_str = raw_input('Please input need string: ')
print recu(convert(calc_str))
























