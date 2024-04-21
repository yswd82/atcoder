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
    A[i] = list(input())

swap = []

print(A)

B = A.copy()


for i in range(N-1):
    B[0][i+1] = A[0][i]
# for i in range(N-1):
    # B[i+1][N-1] = A[i][N-1]
# for i in range(N-1):
    # B[N-1][i] = A[N-1][i+1]
# for i in range(N-1):
    # B[i][0] = A[i+1][0]


print(B)

# for line in B:
#     print(line)