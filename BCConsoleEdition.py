'''
  通常由两个人玩，一方出数字，一方猜。出数字的人要想好一个没有重复数字的4个数，
  
不能让猜的人知道。猜的人就可以开始猜。每猜一个数字，出数者就要根据这个数字给

出几A几B，其中A前面的数字表示位置正确的数的个数，而B前的数字表示数字正确而位

置不对的数的个数。如正确答案为 5234，而猜的人猜 5346，则是 1A2B，其中有一个

5的位置对了，记为1A，而3和4这两个数字对了，而位置没对，因此记为 2B，合起来就

是 1A2B。接着猜的人再根据出题者的几A几B继续猜，直到猜中（即 4A0B）为止。
'''
import re
import sys

def IsInputNumOK(str0):
    if (len(str0)!=4):
        return False
    str1 =  re.findall(r'\d+',str0)
    if( str1==[]):return False
    if (len(str1[0])!=4):
        return False
    for i in str1[0]:
        if len(re.findall(i,str0)) >1:
            return False
    return True

def ABNum(a,b):
    A= 0
    B=0
    for i in range(4):
        if(a[i]==b[i]):
            A = A+1
        if b[i] in a:
            B=B+1
    B= B-A
    print(A,"A",B,"B")
    return A
def GetNum():
    FourNumStr = input('请输入一个四位数:')
    if(not IsInputNumOK(FourNumStr)):
        print("enter miss")
        FourNumStr = GetNum()
    FourNum=[]
    for num in FourNumStr:
         FourNum.append( int(num));
    return FourNum
def CreatNum():
    a = []
    while (len(a) < 4):
        x = random.randint(0, 9)
        if x not in a:
            a.append(x)
    print("New Num has created")
    return a
    
def GameMain():
    n = input('欢迎来到这个游戏\n \n1.规则\n \n2.开始游戏\n \n3.退出游戏\n \n请选择（输入数字）:')
      
    if n == '1':
        
        print('''
游戏规则很简单,就是猜数字游戏，直到猜对位置，随机给出四个数，且不重复。
根据系统的提示，猜对数字和数字位置则为A,猜对数字而没猜对位置则为B。\n
如：如果给出的数字为5246，你猜的数为5678，则会报出1A1B，因为5是位
置和数字都猜对了，另一个是6只猜对了数字没猜对位置，其他是位置和数字
都没猜对，所以为0A0B。聪明的你明白规则了吗？明白了咱们就开始吧''')

    elif n =='2':
        Num0 = CreatNum()
        time = 7
        while(time>0):
            Num1 = GetNum()
            if(ABNum(Num0,Num1)==4):
                print("Win")
                GameMain()
            time=time-1
            print("chance",time)
        print("Lose")
        print("Ture Answer:",Num0)
                

    elif n == '3':
        print('*'*50)
        print('欢迎下次光临')
        print('*'*50)
        quit()
        sys.exit()
    else :
        print("Enter again")
        GameMain()
      
    
    
import random 

if __name__ == '__main__' :
    print('*'*50)
    print('--------欢迎加入 bulls and cows 这个游戏---------')
    print('*'*50)
    print('\n')
    while True:
        GameMain()
        
