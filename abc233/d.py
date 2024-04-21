# N = int(input())
import itertools
from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))
# B = []
# for i in range(N):
#     B.append(int(input()))
# ans = False
# print('Yes') if ans else print('No')

# 累積和
C = list(itertools.accumulate(A))
d = defaultdict(int)

# 先頭に0を足して、それより前の区間の累積和にする
C = [0] + C

print(A)
print(C)

# l...rまでの区間和 = rまでの累積和 - l-1までの累積和
# K = S[r] - S[l-1]
# S[l-1] = S[r] - K
cnt = 0

# rの範囲を探す
for r in range(1, N+1):
    # 累積和の個数
    d[C[r-1]] += 1

    tgt = C[r] - K

    # これまでに発生した累積和の総数から、
    # 累積和がtgtになる個数を数える
    cnt += d[tgt]

    print(r, C[r], K, tgt, d, cnt)

print(cnt)
