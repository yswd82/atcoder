N = int(input())
# N, M = map(int, input().split())
T = input()
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

# 初期状態
dx = 1
dy = 0

x = 0
y = 0

for t in list(T):
    if t == 'S':
        x += dx
        y += dy
    else:
        if (dx, dy) == (1, 0):
            dx, dy = 0, -1
        elif (dx, dy) == (0, -1):
            dx, dy = -1, 0
        elif (dx, dy) == (-1, 0):
            dx, dy = 0, 1
        elif (dx, dy) == (0, 1):
            dx, dy = 1, 0

print(x, y)
