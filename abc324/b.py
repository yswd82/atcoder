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

N = int(input())

ans = False

for x in range(100):
    if 2**x > N:
        break

    for y in range(100):
        if 2**x * 3**y == N:
            ans = True
        if 2**x * 3**y > N:
            break

print("Yes") if ans else print("No")
