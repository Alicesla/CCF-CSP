#将字符串转换为数组
def trans(string,arry):
    j=0
    for i in string:
        if i !=' ' :
            arry[j]=eval(i)
            j+=1
    return arry

#判断name是否已经获胜
def win_B(qipan,name):
    if name in qipan[0]:
        if qipan[0][0]==name:
            if qipan[0][1]==name and qipan[0][2]==name:
                return True
            elif qipan[1][1]==name and  qipan[2][2]==name:
                return True
            elif qipan[1][0]==name and qipan[2][0]==name:
                return True
            else:
                return False
        if qipan[0][1]==name:
            if qipan[1][1]==name and qipan[2][1]==name:
                return True
            else:
                return False
        if qipan[0][2]==name:
            if qipan[1][1]==name and qipan[2][0]==name:
                return True
            elif qipan[1][2]==name and qipan[2][2]==name:
                return True
            else:
                return False
    elif qipan [1][0]==name:
        if qipan[1][2]==name and qipan [1][1]==name:
            return True
        else:
            return False
    elif qipan [2][0]==name:
        if qipan[2][2]==name and qipan [2][1]==name:
            return True
        else:
            return False
    else:
        return False
#统计棋盘中零的个数
def sum_0(qipan):
    sum_0=0
    for i in range(3):
        for j in range(3):
            if qipan[i][j]==0:
                sum_0+=1
    return sum_0
#判断ALICE走一步是否能获胜
def win_A (qipan):
    if (qipan[0][0],qipan[0][1],qipan[0][2])in ((0,1,1),(1,0,1),(1,1,0)):
        return True
    elif (qipan[1][0],qipan[1][1],qipan[1][2])in ((0,1,1),(1,0,1),(1,1,0)):
        return True
    elif (qipan[2][0],qipan[2][1],qipan[2][2])in ((0,1,1),(1,0,1),(1,1,0)):
        return True
    elif (qipan[0][0],qipan[1][0],qipan[2][0])in ((0,1,1),(1,0,1),(1,1,0)):
        return True
    elif (qipan[0][1],qipan[1][1],qipan[2][1])in ((0,1,1),(1,0,1),(1,1,0)):
        return True
    elif (qipan[0][2],qipan[1][2],qipan[2][2])in ((0,1,1),(1,0,1),(1,1,0)):
        return True
    elif (qipan[0][0],qipan[1][1],qipan[2][2])in ((0,1,1),(1,0,1),(1,1,0)):
        return True
    elif (qipan[0][2],qipan[1][1],qipan[2][0])in ((0,1,1),(1,0,1),(1,1,0)):
        return True
    else:
        return False
        
a=int(input())#记录组数
arry=[0 for i in range (3*a)]#记录a组数中的每一行
for i in range(3*a):
    arry[i]=input()

for i in range(1,1+a):
    qipan = [[0 for i in range(3)]for i in range(3)]
    for j in range(1,4):
        qipan[j-1]=trans(arry[(i-1)*3+j-1],qipan[j-1])
    if win_B(qipan,2):#如果Bob赢得比赛
        print(0-sum_0(qipan)-1)
    elif win_A(qipan):#如果Alice再走一步赢得比赛
        print(sum_0(qipan))
    else:
        print(0)
        

