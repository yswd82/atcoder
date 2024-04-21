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
N, L = map(int, input().split())
A = list(map(int, input().split()))

passes = sum([1 if a >= L else 0 for a in A])
print(passes)
