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

A = [None] * N


for i in range(N):
    A[i] = list(map(int, input().split()))


for i in range(N):
    x = []
    for j in range(N):
        if A[i][j]:
            x.append(j + 1)

    print(*x)
