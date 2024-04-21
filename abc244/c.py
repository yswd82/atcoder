N = int(input())
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

zenbu = set(range(1, N * 2 + 1 + 1))

while len(zenbu) > 0:
    taka = min(zenbu)
    print(taka)
    zenbu.remove(taka)

    if len(zenbu) == 0:
        break

    aoki = int(input())
    zenbu.remove(aoki)

    if len(zenbu) == 0:
        break

input(int(0))
