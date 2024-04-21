from itertools import product
N = int(input)
X, Y = map(int, input().split())

A, B = [], []

for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

# 無理な場合
if sum(A) < X or sum(B) < Y:
    print(-1)
    exit()

# 多い順にX, Y必要な個数を数える
a_ = 0
a_cnt = -1
for i, a in enumerate(sorted(A, reverse=True)):
    a_ += a
    if a_ >= X:
        a_cnt = i + 1

b_ = 0
b_cnt = -1
for i, b in enumerate(sorted(B, reverse=True)):
    b_ += b
    if b_ >= X:
        b_cnt = i + 1

# 最低でも買う個数
buy_min = max(a_cnt, b_cnt)


