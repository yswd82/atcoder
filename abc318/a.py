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
N, M, P = map(int, input().split())


ans = [1 for x in range(1, 2 * 10**5 + 1) if x <= N and (x - M) % P == 0 and M <= x]

print(sum(ans))
