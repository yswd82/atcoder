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
