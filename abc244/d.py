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
S = input().split()
T = input().split()

cnt = 0
for s, t in zip(S, T):
    if s != t:
        cnt += 1

if cnt in (0, 3):
    print('Yes')
else:
    print('No')
