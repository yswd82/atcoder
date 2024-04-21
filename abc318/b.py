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
A = [0] * N
B = [0] * N
C = [0] * N
D = [0] * N

for i in range(N):
    A[i], B[i], C[i], D[i] = map(int, input().split())

area = [[0] * 100 for n in range(100)]

for i in range(N):
    for x in range(A[i], B[i]):
        for y in range(C[i], D[i]):
            if area[x][y] == 0:
                area[x][y] = 1

ans = 0
for l in area:
    ans += sum(l)
print(ans)