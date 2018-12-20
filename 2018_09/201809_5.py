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
s=arry[0]
K=[0 for i in range (s)]
K=trans(str_2,K)
l=arry[1]
r=arry[2]
A=[0 for i in range(r+1)]
A[0]=1

for i in range (l-s,r+1):
    for j in range(s):#s是10**3
        if i>j:
            A[i]=A[i]+K[j]*A[i-j-1]
            if A[i]>=998244353:
                A[i]=A[i]%998244353
        else:
            break
    if i>=l:
        print(A[i])

