import sys
import math

if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])

import itertools
N, X = map(int, input().split())

# A = list(map(int, input().split()))
L = [None] * N
a = [None] * N
for i in range(N):
    l = list(map(int, input().split()))
    L[i] = l[0]
    a[i] = l[1:]

# アンパックしてproductを使う
p = itertools.product(*a)

cnt = 0

for v in p:
    if math.prod(v) == X:
        cnt += 1

print(cnt)
