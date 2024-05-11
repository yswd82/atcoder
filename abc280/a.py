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
S = [0] * H
for i in range(H):
    S[i] = list(input())

cnt=0
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            cnt+=1
print(cnt)
