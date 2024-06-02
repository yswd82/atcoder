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
n = int(input())
h = list(map(int, input().split()))

maxh = h[0]

for i in range(1,n):
    if h[i-1] < h[i]:
        maxh = max(maxh, h[i])
    else:
        break

print(maxh)