# N = int(input())
# N, M = map(int, input().split())

# A = list(map(int, input().split()))

# B = []
# for i in range(N):
#     B.append(int(input()))

# S = []
# for i in range(N):
#     S.append(input())

# ans = False
# print('Yes') if ans else print('No')

N = int(input())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

# iが一番上にいる場合の高さをCとする
C = [0] * N
Cmax = 0
Asum = sum(A)
for i in range(N):
    C[i] = Asum - A[i] + B[i]

    if Cmax < C[i]:
        Cmax = C[i]

print(Cmax)

