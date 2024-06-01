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
from decimal import Decimal, ROUND_HALF_UP

X = float(input())

a = Decimal(X).quantize(Decimal('0'), ROUND_HALF_UP)

print(a)