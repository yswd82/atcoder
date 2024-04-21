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

X, Y = map(int, input().split())

if (X < Y and Y - X <= 2) or (X > Y and X - Y <= 3):
    print("Yes")
else:
    print("No")
