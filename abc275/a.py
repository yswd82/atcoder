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
H = list(map(int, input().split()))

highest = -1
hmax = 0

for i in range(N):
    if H[i] > hmax:
        highest = i+1
        hmax = H[i]

print(highest)