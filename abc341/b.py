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
A = list(map(int, input().split()))
S = [None] * N
T = [None] * N
for i in range(N - 1):
    S[i], T[i] = map(int, input().split())

for i in range(N - 1):
    count = A[i] // S[i]

    A[i] -= S[i] * count
    A[i + 1] += T[i] * count

# i = N - 2
# count = A[i] // S[i]
# A[i] -= S[i] * count
# A[i + 1] += T[i] * count

print(A[i + 1])
