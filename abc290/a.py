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
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(sum([ A[i] for i in range(N) if i+1 in B]))
