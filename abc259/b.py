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
a,b,d=map(int, input().split())

import numpy as np


# ベクトル回転関数
# deg=Falseならばラジアンで角度を指定
# deg=Trueならば度数単位で角度を指定
def rotation_o(u, t, deg=False):

    # 度数単位の角度をラジアンに変換
    if deg == True:
        t = np.deg2rad(t)

    # 回転行列
    R = np.array([[np.cos(t), -np.sin(t)],
                  [np.sin(t),  np.cos(t)]])

    return  np.dot(R, u)

# 単位ベクトル
u = (a, b)

# uを回転させる
Ru = rotation_o(u, d, deg=True)

print(*Ru)