#将字符串转换为数组
def trans(string):
    flag=0
    j=0
    arry=[0 for i in range(2)]
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
#将字符串转换为二维数组
def stoa(string):
    arry=[]
    flag=0#用来计算连续.的个数
    ind=0#用来计算遍历字符串位置
    L=0#用来记录左侧字符
    R=0#用来记录右侧字符位置
    if string[0]!='.':
        arry.append(string.lower())
        return arry
    else:
        for i in string:
            ind+=1
            if i=='.':
                L+=1
                flag+=1
                if flag==2:
                    arry.append('..')
                    flag=0
            elif i==' ':
                R=ind
                arry.append(string[L:R-1].lower())
                L=ind
            elif ind==len(string):
                R=ind
                if string[L]=='#':
                    arry.append(string[L:R])
                else:
                    arry.append(string[L:R].lower())
                L=ind
            else:
                continue
        return arry
def stoa_2(string):
    arry=[]
    R=0
    ind=0
    for i in string:
        L=R
        ind+=1
        if i==' ':
            R=ind
            arry.append(string[L:R-1].lower())
        elif ind==len(string):
            R=ind
            if string[L]=='#':
                    arry.append(string[L:R])
            else:
                arry.append(string[L:R].lower())
        else:
            continue
    return arry
           
#main
line_1=trans(input())
con=[0 for i in range(line_1[0])]
req=[0 for i in range(line_1[1])]
for i in range(line_1[0]):
    con[i]=stoa(input())
for i in range(line_1[1]):
    req[i]=stoa_2(input())
for i in range(1,line_1[0]):
    for j in range(len(con[i])):
        if con[i][j]=='..':
            con[i][j]=con[i-1][j]
for i in range(line_1[1]):
    times=0
    arry=[]
    for j in range(line_1[0]):
        for k in range(len(con[j])):
            if req[i][0]==con[j][k]:
                if len(req[i])==1:
                    times+=1
                    arry.append(j+1)
                else:
                    for m in range(1,len(req[i])):
                        if k+m<len(con[j]):
                            if req[i][m]==con[j][k+m]:
                                if m==len(req[i])-1:
                                    times+=1
                                    arry.append(j+1)
                            else:
                                break
    print (times,end=' ')
    for i in range(len(arry)):
        print(arry[i],end=' ')
    print()















    
