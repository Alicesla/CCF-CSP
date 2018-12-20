def trans(string,arry):#将字符串转换为数组
    flag=0
    j=0
    for i in string:
        if flag==0 and i !=' ' :
            arry[j]=eval(i)
            j+=1
            flag=1
        elif i==' ':
            flag=0
        else:
            j-=1
            arry[j]=arry[j]*10+int(eval(i))
            j+=1
    return arry

str_1=input()
str_2=input()
arry=[0 for i in range(3)]
arry=trans(str_1,arry)
print(arry)
pos=[0 for i in range(arry[0])]
pos=trans(str_2,pos)
ind=[1 for i in range(arry[0])]
for i in range(arry[2]):
    for j in range(arry[0]):
        pos[j]=pos[j]+ind[j]
    if arry[1] in pos :
        ind[pos.index(arry[1])]=-ind[pos.index(arry[1])]
    if 0 in pos:
        ind[pos.index(0)]=-ind[pos.index(0)]
    if len(set(pos))<arry[0]:
        for k in range(arry[0]-1):
            for l in range(k+1,arry[0]):
                if pos[k]==pos[l]:
                    ind[k]=-ind[k]
                    ind[l]=-ind[l]
                    break

for i in range(arry[0]):
    print(pos[i],end=' ')
