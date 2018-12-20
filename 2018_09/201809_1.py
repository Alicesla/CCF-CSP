#计算平均数
def avg(arry):
    b=[0 for i in range(len(arry))]
    for i in range(len(arry)):
        if i==0:
            b[0]=int((arry[0]+arry[1])/2)
        elif i==len(arry)-1:
            b[i]=int((arry[i]+arry[i-1])/2)
        else:
            b[i]=int((arry[i-1]+arry[i]+arry[i+1])/3)
    return b


#a代表商店数量
a=int(input())
#arry存储商店第一天菜价
arry=[0 for i in range(a)]
#str_arry 是字符串形式的第一天的菜价
str_arry=input()
j=0
flag=0
#将第一天菜价由字符串转变成数组形式
for i in str_arry:
    if i !=' ' and flag==0:
        arry[j]=eval(i)
        j+=1
        flag=1
    elif i==' ':
        flag=0
    else:
        j-=1
        arry[j]=arry[j]*10+int(eval(i))
        j+=1
arry=avg(arry)
#按照格式输出
for i in range(a):
    print (arry[i],end=' ')



