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
N, H,X = map(int, input().split())

P = list(map(int, input().split()))

for i in range(N):
    if X <= H + P[i]:
        print(i+1)
        exit()
