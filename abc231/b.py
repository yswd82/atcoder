import collections
N = int(input())

S = []
for i in range(N):
    S.append(input())


c = collections.Counter(S)

max_k = 0
ans = ''

for k, v in c.items():
    if max_k < v:
        max_k = v
        ans = k

print(ans)
