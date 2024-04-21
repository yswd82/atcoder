# N = int(input())
N, M, K, S, T, X = map(int, input().split())
MOD = 998244353

# 頂点番号にするため-1
S -= 1
T -= 1
X -= 1

# A = list(map(int, input().split()))
#
# B = []

U = [None] * M
V = [None] * M
for i in range(M):
    u, v = map(int, input().split())
    U[i], V[i] = u-1, v-1

# dp[i][j] 頂点Sから辺をi回通って頂点jへ行く方法
# i ... K+1
# j ... N

# 頂点Xを通った回数がmod 2がx

# dp = [[[0] * 2 for i in range(N)] for i in range(K+1)]
dp = [[[0] * N for i in range(K+1)] for x in range(2)]

# 初期状態
# Sから辺をk(0回)通ってSへ行き、Xを通る回数はx(0回)のルートは1個
# dp[x][k][S] = 1
dp[0][0][S] = 1

for i in range(K):
    for u, v in zip(U, V):
        for x in range(2):
            # vからuに行く
            # vがXだったら通った回数が+1するので, xが1なら0(偶数), xが0なら1(奇数)にする
            dp[x][i+1][u] += dp[x ^ (v == X)][i][v]
            if dp[x][i+1][u] >= MOD:
                dp[x][i+1][u] -= MOD

            # 逆方向
            dp[x][i+1][v] += dp[x ^ (u == X)][i][u]
            if dp[x][i+1][v] >= MOD:
                dp[x][i+1][v] -= MOD

            # print(dp)
print(dp[0][K][T])
