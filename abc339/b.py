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
import math

H, W, N = map(int, input().split())

taka_h = int(0)
taka_w = int(0)
# taka_dir = 90
taka_dir = math.pi * 1 / 2

MAP = [["."] * W for i in range(H)]


for i in range(N):
    if MAP[taka_h][taka_w] == ".":
        MAP[taka_h][taka_w] = "#"
        taka_dir -= math.pi * 1 / 2
    else:
        MAP[taka_h][taka_w] = "."
        taka_dir += math.pi * 1 / 2

    taka_h -= int(math.sin(taka_dir))
    taka_w += int(math.cos(taka_dir))

    taka_h = taka_h % H
    taka_w = taka_w % W


for i in range(H):
    print("".join(MAP[i]))
