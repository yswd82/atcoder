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
M, D = map(int, input().split())
y, m, d = map(int, input().split())


if d + 1 > D:
    m += 1
    d = 1
else:
    d += 1

if m > M:
    y += 1
    m = 1

print(y, m, d)
