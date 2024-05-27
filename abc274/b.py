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
C = [0] * H
for i in range(H):
    C[i] = input()

cnt = [0] * W
for j in range(W):
    for i in range(H):
        if C[i][j] == '#':
            cnt[j] += 1

print(*cnt)

