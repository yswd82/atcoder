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

a_msk = [0] * m
for j in range(m):
    for l in range(c[j]):
        a_msk[j] += 2 ** (a[j][l]-1)
# print(a_msk)
ans = 0

# 2**N 通りのすべての正誤パターンに対して
for i in range(2 ** n):
    # すべてのテストにパスすると仮定して
    ok = 1

    # すべてのテストをする
    for j in range(m):
        # 挿した鍵を数値化してパターンとのand演算をする
        mask = bin( i & a_msk[j])
        corrects = mask.count('1')

        # 開いたとき、k個以上の正解キーがあるはず
        # 開かないとき、k個未満の正解キーがあるはず
        if not(( r[j] == 'o' and corrects >= k ) or ( r[j] == 'x' and corrects < k )):
            # 条件を満たさないパターンはパスしない
            ok = 0
    ans+=ok
print(ans)            
