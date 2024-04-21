import math
X, Y = map(int, input().split())
# A = list(map(int, input().split()))
# B = []
# for i in range(N):
#     B.append(int(input()))
# ans = False
# print('Yes') if ans else print('No')

ans = math.ceil((Y - X) / 10)
print(max(ans, 0))
