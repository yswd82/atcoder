# N = int(input())
# N, M = map(int, input().split())

# A = list(map(int, input().split()))

# B = []
# for i in range(N):
#     B.append(int(input()))

# S = []
# for i in range(N):
#     S.append(input())

# ans = False
# print('Yes') if ans else print('No')
import math

n = int(input())
x=[0]*n
y=[0]*n
for i in range(n):
    x[i], y[i] = map(int, input().split())

maxlen=0

for i in range(n):
    for j in range(i, n):
        maxlen = max(math.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2 ), maxlen)

print(maxlen)