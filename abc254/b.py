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
n=int(input())

from math import *

def calc(k):
    return [ factorial(k)/(factorial(i)*factorial(k-i)) for i in range(k+1)]

for i in range(n):
    print(*map(int, calc(i)))
