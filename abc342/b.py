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
P = list(map(int, input().split()))
Q = int(input())

A = [None] * Q
B = [None] * Q
for i in range(Q):
    A[i], B[i] = map(int, input().split())


for i in range(Q):
    posa = P.index(A[i])
    posb = P.index(B[i])

    if posa < posb:
        ans = A[i]
    else:
        ans = B[i]

    print(ans)
