# N = int(input())
# N, M = map(int, input().split())
#
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

S = list(map(int, input().split()))

if S == sorted(S) and 100 <= min(S) and max(S) <= 675 and all([ True if s % 25 == 0 else False for s in S]):
    ans = True
else:
    ans = False

print('Yes') if ans else print('No')