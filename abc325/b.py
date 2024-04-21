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

N = int(input())

W = [None] * N
X = [None] * N
for i in range(N):
    W[i], X[i] = map(int, input().split())

pmax = 0
for h in range(24):
    p = 0
    for i in range(N):
        xh = (X[i] + h) % 24
        if 9 <= xh <= 17:
            p += W[i]

    pmax = max(pmax, p)

print(pmax)
