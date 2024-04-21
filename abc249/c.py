# N = int(input())
N, K = map(int, input().split())
#
# A = list(map(int, input().split()))
#
# B = []
# for i in range(N):
#     B.append(int(input()))
#
S = []
for i in range(N):
    S.append(input())

x = ''
for s in S:
    x = x + s

sset = []
for i in range(N):
    sset.append(set(S[i]))

all_chars = set(x)

# print(all_chars)

chr_cnt = {}
for c in all_chars:
    chr_cnt.update({c:0})

# print(chr_cnt)

import collections
import itertools
from collections import defaultdict

cnts = []
for i in range(N):
    cnts.append(collections.Counter(S[i]))

ans_max = 0
import copy

# 2 ** 15通り
for combi in list(itertools.product([0,1], repeat=N)):

    _chr_cnt = copy.deepcopy(chr_cnt)

    # N
    for i, tf in enumerate(combi):
        if tf == 1:
            for k, v in cnts[i].items():
                _chr_cnt[k] += 1

    ans = 0
    for k,v in _chr_cnt.items():
        if v == K and v > 0:
            ans += 1
    if ans > ans_max:
        ans_max = ans

        # print(i, chr_cnt, ans_max)

print(ans_max)