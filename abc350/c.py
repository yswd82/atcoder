n=int(input())
a=list(map(int, input().split()))
d = dict()
for i,v in enumerate(a):
    d.update({v:i})

changes = []
sort_a = sorted(a)
for i in range(n):
    j = d[i+1]
    if a[i] != a[j] and i<j:
        changes.append(sorted([i+1,j+1]))
        a[i],a[j] = a[j],a[i]
    if a == sort_a:
        break

print(len(changes))
for c in changes:
    print(*c)