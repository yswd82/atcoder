# N = int(input())
# N, M = map(int, input().split())
#
# A = list(map(int, input().split()))
#
# B = []
# for i in range(N):
#     B.append(int(input()))
#
# S = []
# for i in range(N):
#     S.append(input())
#
# ans = False
# print('Yes') if ans else print('No')
n,x,y,z=map(int, input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))

class Person():
    def __init__(self,i,a,b) -> None:
        self.i = i
        self.a = a
        self.b = b
        self.ab = a+b
        self.a_gou = 0
        self.b_gou = 0
        self.ab_gou = 0

persons =[None]*n
goukaku = []

for i in range(n):
    persons[i] = Person(i,a[i],b[i])


a_gou = []
b_gou = []
ab_gou = []

cnt=0
gokakuten = 100

while cnt < x:
    for p in persons:
        if cnt < x and p.a_gou == 0 and gokakuten <= p.a:
            p.a_gou=1
            # print('agou',  p.i+1)
            a_gou.append(p.i+1)
            cnt+=1
    gokakuten-=1

cnt=0
gokakuten = 100

while cnt < y:
    for p in persons:
        if cnt < y and p.a_gou == 0 and p.b_gou == 0 and gokakuten <= p.b:
            p.b_gou=1
            # print('bgou', p.i+1)
            b_gou.append(p.i+1)
            cnt+=1
    gokakuten-=1

cnt=0
gokakuten = 200

while cnt < z:
    for p in persons:
        if cnt < z and  p.a_gou == 0 and p.b_gou == 0  and p.ab_gou == 0 and gokakuten <= p.ab:
            p.ab_gou=1
            # print('abgou',p.i+1)
            ab_gou.append(p.i+1)
            cnt+=1
    gokakuten-=1

ans = a_gou + b_gou + ab_gou
print(*sorted(ans))