def comp(arr):
        arr_1=list(arr)
        arr_2=[]
        num=''
        arr_4=[]
        for i in arr_1:
                if i not in ['+','-','*','/']:
                        num += i
                else:
                        arr_2.append(num)
                        arr_4.append(i)
                        num=''
        arr_2.append(num)
        fis = int(arr_2[0])
        for j in range(len(arr_4)):
                if arr_4[j]=='+':
                        fis += int(arr_2[j+1])
                elif arr_4[j]=='-':
                        fis -= int(arr_2[j+1])
                elif arr_4[j]=='*':
                        fis *= int(arr_2[j+1])
                else:
                        fis /= int(arr_2[j+1])
        return fis
num_input =raw_input('please your str:')
print '%s==%s '%(num_input,comp(num_input))
