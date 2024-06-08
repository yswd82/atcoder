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
n,m,t=map(int, input().split())
a=list(map(int, input().split()))
x=[0]*m
y=[0]*m

for i in range(m):
    x[i],y[i] = map(int,input().split())

bonus = [0] * n
for i in range(m):
    bonus[x[i]-1] = y[i]

room = [0] * n
room[0] = t

for i in range(1,n):
    if room[i-1] - a[i-1] <= 0:
        print('No')
        exit()
    else:
        room[i] = room[i-1] - a[i-1] + bonus[i]
print('Yes')

