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

N, S, K = map(int, input().split())

P = [None] * N
Q = [None] * N

for i in range(N):
    P[i], Q[i] = map(int, input().split())

price = 0
for i in range(N):
    price += P[i] * Q[i]

if S <= price:
    print(price)
else:
    print(price + K)
