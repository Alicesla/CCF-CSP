#a为时间段数量
a=int (input())
#str_H为小H和小W装车时间段字符串形式
str_H=[0 for i in range(2*a)]
for i in range(2*a):
    str_H[i]=input()
    
H=[]
W=[]
k=0
#将字符串转换为数组
for i in range(2*a):
    flag=0
    for j in str_H[i]:
        if j !=' ' and flag==0:
            H.append(eval(j))
            k+=1
            flag=1
        elif j==' ':
            flag=0
        else:
            k-=1
            H[k]=H[k]*10+int(eval(j))
            k+=1
for i in range (4*a):
    if i%2==0:
        for j in range(H[i],H[i+1]):
            W.append(j)
times_1=len(W)
W=list(set(W))
times_2=len(W)
print(times_1-times_2)
        
