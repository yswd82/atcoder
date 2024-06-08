# N = int(input())
# N, M = map(int, input().split())

# A = list(map(int, input().split()))

# B = []
# for i in range(N):
#     B.append(int(input()))

# S = []
# for i in range(N):
#     S.append(input())

# pattern = False
# print('Yes') if pattern else print('No')
n,m,k=map(int, input().split())
c=[0]*m
r=[0]*m
a=[0]*m
for i in range(m):
    tmp = input().split()
    c[i] = tmp[0]
    a[i] = tmp[1:-1]
    r[i] = tmp[-1]
c = list(map(int, c))
a = [ list(map(int,_a)) for _a in a ]

from itertools import product

pattern = [0] * m
allpat = [ bit for bit in product([0, 1], repeat=n)]

for i in range(m):
    # 挿した鍵の数が必要数以上のとき(必要数未満だと必ず開かないので情報がない)
    if c[i] >= k:

        # すべてのパターンに対して
        bits = []
        for bit in allpat:
            # 開いたとき
            if r[i] == 'o':
                # 試行した鍵の中に含まれる正解数が少なくともk以上かつ
                if sum([ 1 if bit[a[i][j] - 1] == 1 else 0 for j in range(c[i])]) >= k:
                    # 正解数の合計がk以上になる組み合わせがあり得る
                    if sum(bit) >= k:
                        bits.append(bit)

            # 開かなかったとき
            if r[i] == 'x':
                # 試行した鍵の中に含まれる正解数はK個未満であることがわかる
                if sum([ 1 if bit[a[i][j] - 1] == 1 else 0 for j in range(c[i])]) < k:
                    # 正解数の合計がk以上になる組み合わせがあり得る
                    if sum(bit) >= k:
                        bits.append(bit)

        pattern[i] = bits

        # print(pattern[i])

# すべての試行のパターンに共通する要素の個数を数える
ans = set(pattern[0])
for pattern_ in pattern:
    ans = ans & set(pattern_)
print(len(ans))


