N, M = map(int, input().split())
k = [None]*M
x = [None]*M

for m in range(M):
    tmp = list(map(int, input().split()))

    k[m] = tmp[0]
    x[m] = tmp[1:]

p = set()

for n1 in range(N):
    for n2 in range(n1,N):
        if n1 != n2:
            p.add((n1+1,n2+1))


for m in range(M):
    for _1 in x[m]:
        for _2 in x[m]:
            if _1 < _2:
                try:
                    p.remove((_1,_2))
                except:
                    pass
    
if p:
    print("No")
else:
    print("Yes")
