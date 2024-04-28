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
H, W = map(int, input().split())

S = [None] * H

snuke = ["s", "n", "u", "k", "e"]

for i in range(H):
    S[i] = input()

ans = []


for i in range(H):
    for j in range(W):
        if S[i][j] == 's':
            flg_r = j <= W - 5
            flg_l = 4 <= j
            flg_d = i <= H - 5
            flg_u = 4 <= i

            # 右方向
            if flg_r:
                ans_r = all([S[i][j+k] == snuke[k] for k in range(5)])
                if ans_r:
                    ans.append((i,j))
                    ans_dir = (0,1)

            # 左方向
            if flg_l:
                ans_l = all([S[i][j-k] == snuke[k] for k in range(5)])
                if ans_l:
                    ans.append((i,j))
                    ans_dir = (0,-1)

            # 下方向
            if flg_d:
                ans_d = all([S[i+k][j] == snuke[k] for k in range(5)])
                if ans_d:
                    ans.append((i,j))
                    ans_dir = (1,0)

            # 上方向
            if flg_u:
                ans_u = all([S[i-k][j] == snuke[k] for k in range(5)])
                if ans_u:
                    ans.append((i,j))
                    ans_dir = (-1,0)

            # 右下方向
            if flg_r and flg_d:
                ans_rd = all([S[i+k][j+k] == snuke[k] for k in range(5)])
                if ans_rd:
                    ans.append((i,j))
                    ans_dir = (1,1)

            # 右上方向
            if flg_r and flg_u:
                ans_ru = all([S[i-k][j+k] == snuke[k] for k in range(5)])
                if ans_ru:
                    ans.append((i,j))
                    ans_dir = (-1,1)

            # 左下方向
            if flg_l and flg_d:
                ans_ld = all([S[i+k][j-k] == snuke[k] for k in range(5)])
                if ans_ld:
                    ans.append((i,j))
                    ans_dir = (1,-1)

            # 左上方向
            if flg_l and flg_u:
                ans_lu = all([S[i-k][j-k] == snuke[k] for k in range(5)])
                if ans_lu:
                    ans.append((i,j))
                    ans_dir = (-1,-1)

ans = ans[0]
x = ans[0] + 1
y = ans[1] + 1
for i in range(5):
    print(x, y)
    x += ans_dir[0]
    y += ans_dir[1]


