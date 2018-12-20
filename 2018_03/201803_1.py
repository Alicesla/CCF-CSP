def trans(string,arry):#将字符串转换为数组
    j=0
    for i in string:
        if i !=' ' :
            arry.append(eval(i))
            j+=1
    return arry
string=input()
arry=[]
sum=0
flag=0
arry=trans(string,arry)
for i in range(len(arry)):
    if arry[i]==0:
        break
    elif arry[i]==1:
        sum+=1
        flag=0
    else:
        flag+=1
        sum=sum+2*flag
print (sum)
