# N = int(input())
n,t = map(int, input().split())

a = list(map(int, input().split()))

# B = []
# for i in range(N):
#     B.append(int(input()))

# S = []
# for i in range(N):
#     S.append(input())

# ans = False
# print('Yes') if ans else print('No')

# b = [[None] * n for i in range(n)]
yoko = [0] * n
tate = [0] * n
naname1 = 0
naname2 = 0
for i in range(n):
    for j in range(n):
        yoko[i] += n * i + (j+1)
        tate[j] += n * i + (j+1)

        if i == j:
            naname1+=n * i + (j+1)
        if i+j == n-1:
            naname2+=n * i + (j+1)

# print(yoko)
# print(tate)

for k in range(t):
    # 呼ばれた数字を0にする
    i = (a[k]-1) // n
    j = (a[k]-1) % n

    # print(a[k])

    # b[i][j] = 0
    # print(yoko[i], a[k])
    yoko[i] -= a[k]
    if yoko[i] == 0:
        print(k+1)
        exit()
    tate[j] -= a[k]
    if tate[j] == 0:
        print(k+1)
        exit()

    if i == j:
        naname1-=a[k]
        if naname1 == 0:
            print(k+1)
            exit()
    if i+j == n-1:
        naname2-=a[k]
        if naname2 == 0:
            print(k+1)
            exit()


    # # print(b)

    # # 呼ばれた数字に関連する縦横斜めの合計を確かめる
    # # 横
    # if sum(b[i]) == 0:
    #     print(k+1)
    #     exit()

    # # たて
    # tate = 0
    # for l in range(n):
    #     tate += b[l][j]

    # if tate == 0:
    #     print(k+1)
    #     exit()

    # # ななめ
    # if i == j or i+j == n-1:
    #     naname1 = 0
    #     naname2 = 0
    #     for l in range(n):
    #         naname1+=b[l][l]
    #         naname2+=b[l][n-l-1]

    #     if naname1 == 0:
    #         print(k+1)
    #         exit()
    #     if naname2 == 0:
    #         print(k+1)
    #         exit()

print(-1)
