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

H,W = map(int, input().split())

A = [None] * H

for i in range(H):
    A[i] = list(map(int, input().split()))


S = [[None] * W for i in range(H)]

for i in range(H):
    for j in range(W):
        if A[i][j] == 0:
            S[i][j] = "."
        else:
            S[i][j] = chr(A[i][j] - 1 + 65)
    
for i in range(H):
    print("".join(S[i]))