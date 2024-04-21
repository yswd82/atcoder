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
K, G, M = map(int, input().split())

g = 0
m = 0

for i in range(K):
    if g == G:
        g = 0
    elif m == 0:
        m = M
    else:
        v = min(m, G - g)
        g += v
        m -= v

print(g, m)
