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

for i in range(N + 1):
    for j in range(N + 1):
        for k in range(N + 1):
            if i + j + k <= N:
                print(i, j, k)
