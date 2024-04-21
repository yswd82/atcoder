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

N, L, R = map(int, input().split())
A = list(map(int, input().split()))

X = [None] * N

for i in range(N):
    X[i] = min([abs(L - A[i]), abs(R - A[i])])

    if A[i] <= L:
        X[i] = A[i] + X[i]
    elif R <= A[i]:
        X[i] = A[i] - X[i]


print(*X)
