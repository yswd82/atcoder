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
n,k=map(int, input().split())
a=list(map(int, input().split()))
x=[0]*n
y=[0]*n
for i in range(n):
    x[i], y[i]=map(int, input().split())

import math

# 光源からの距離
dist = [None]*n

for _a in a:
    for _n in range(n):
        if _a-1 == _n:
            # 自身が光源
            dist[_n] = 0
        else:
            # 最も近い光源との距離をとる
            distance = math.sqrt((x[_a-1] - x[_n])**2 + (y[_a-1] - y[_n])**2)
            if dist[_n] is None:
                dist[_n] = distance
            else:
                dist[_n] = min(dist[_n], distance)
print(max(dist))