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
from typing import List

T:int = int(input())
N:List[int] = [0] * T
A:List[int] = [0] * T


for i in range(T):
    N[i] = int(input())
    A[i] = list(map(int, input().split()))

for i in range(T):
    print(sum([ a % 2 for a in A[i] ]))

