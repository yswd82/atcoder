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
n,k=map(int, input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
oisisamax=0
oisisamax=max(a)
ans = False
for i in range(n):
    if a[i] == oisisamax and i+1 in b:
        ans = True
print('Yes') if ans else print('No')
