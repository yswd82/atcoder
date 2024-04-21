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

N, P,Q = map(int, input().split())

D = list(map(int, input().split()))


if (P-Q) > min(D):
    print(Q+min(D))
else:
    print(P)