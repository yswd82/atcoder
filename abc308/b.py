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
N, M = map(int, input().split())
C = [None] * N
D = [None] * M
P = [0] * (M+1)
C = list(input().split())
D = list(input().split())
P = list(map(int, input().split()))
p0 = P[0]
P = P[1:]

price = {}
for m in range(M):
    price.update(
        {D[m]: P[m]}
    )

p=0
for i in range(N):
    p+=price.get(C[i], p0)

print(p)