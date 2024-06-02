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
h,w= map(int, input().split())
s=[0]*h
for i in range(h):
    s[i] = list(input())
x = []
y = []
for i in range(h):
    for j in range(w):
        if s[i][j] == 'o':
            x.append(i)
            y.append(j)
print(abs(x[0] - x[1]) + abs(y[0] - y[1]))

