def pingjun(arry):
    b=[0 for i in range(len(arry))]
    for i in range(len(arry)):
        if i==0:
            b[0]=int((arry[0]+arry[1])/2)
        elif i==len(arry)-1:
            b[i]=int((arry[i]+arry[i-1])/2)
        else:
            b[i]=int((arry[i-1]+arry[i]+arry[i+1])/3)
    return b

a=int(input())
arry=[0 for i in range(a)]
str_arry=input()
j=0
flag=0
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
arry=pingjun(arry)
for i in range(a):
    print (arry[i],end=' ')



