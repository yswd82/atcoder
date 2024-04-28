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

R,C = map(int, input().split())

B = [None] * R
B2 = [[None] * C for i in range(R)]

for i in range(R):
    B[i] = list(input())

for i in range(R):
    for j in range(C):
        B2[i][j] = B[i][j]

for i in range(R):
    for j in range(C):

        if B[i][j] not in (".", "#"):
            h = int(B[i][j])

            for bi in range(max(0, i - h), min(i+h+1, R)):
                for bj in range(max(0, j - h), min(j+h+1, C)):
                    if (abs(bi-i)+abs(bj-j))<=h:
                        B2[bi][bj] = "."

for i in range(R):
    print("".join(B2[i]))


