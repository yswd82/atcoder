S = input()

import collections

c = collections.Counter(S)

cnt = [0] * 100
for k,v in c.items():
    cnt[v] += 1

ans = True
for c in cnt:
    if c not in (0,2):
        ans = False


print("Yes" if ans else "No")
