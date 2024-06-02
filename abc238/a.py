# N = int(input())
# N, M = map(int, input().split())

# A = list(map(int, input().split()))

# B = []
# for i in range(N):
#     B.append(int(input()))

# S = []
# for i in range(N):
#     S.append(input())

# ans = False
# print('Yes') if ans else print('No')
n=int(input())
if 5 < n:
    ans = True
else:
    ans = n ** 2 < 2 ** n
print('Yes') if ans else print('No')
