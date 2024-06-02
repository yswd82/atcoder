# N = int(input())
# N, M = map(int, input().split())

# A = list(map(int, input().split()))

# B = []
# for i in range(N):
#     B.append(int(input()))

# S = []
# for i in range(N):
#     S.append(input())

# ans = False
# print('Yes') if ans else print('No')
n=int(input())
a=list(map(int,input().split()))

slice = [0]

for i in range(n):
    # 既存の切れ込みを回転させる
    slice = [ _+a[i] for _ in slice ]
    # 新たな切れ込みを加える
    slice.append(0)

# 360度の範囲に直して終点をもう一つ入れる
slice = [ _ % 360 if 360 < _ else _ for _ in slice ] + [360]
slice = sorted(slice)

maxdeg = 0
for i in range(1, len(slice)):
    maxdeg = max(maxdeg, slice[i] - slice[i-1])

print(maxdeg)
