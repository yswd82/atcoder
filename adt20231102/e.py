# その生徒の点数に300点足した点を超える点数の生徒の数=絶対に抜けない生徒の数
n, k = map(int, input().split())

p = [0] * n

# 生徒の合計点
for i in range(n):
    p[i] = sum(map(int, input().split()))

# 降順にソートしてk番目の点数
t = sorted(p, reverse=True)[k - 1]

for i in range(n):
    if p[i] + 300 >= t:
        ans = "Yes"
    else:
        ans = "No"
    print(ans)
