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
from decimal import Decimal

A,B = map(int, input().split())

A = Decimal(A)
B = Decimal(B)

if A % B == 0:
    print(A // B)
else:
    print(A // B + 1)