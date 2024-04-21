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

if N == 1 or max(P[1:]) < P[0]:
    print(0)
else:
    ans = max(P[1:]) - P[0] + 1
    print(ans)