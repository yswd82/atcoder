N,Q= map(int, input().split())

L = [None] * N
a = [None] * N
for i in range(N):
    _ = list(map(int, input().split()))
    L[i] = _[0]
    a[i] = _[1:]
s = [None] * Q
t = [None] * Q

for i in range(Q):
    s[i], t[i] = map(int, input().split())


for k in range(Q):
    ans = a[s[k]-1][t[k]-1]
    print(ans)
    