N, Q = map(int, input().split())

A = list(map(int, input().split()))
x = []
for i in range(Q):
    x.append(int(input()))

sA = sorted(A)
sX = sorted(x)
counts = {}

all_count = len(sA)

start_j = 0
start_cnt = 0

for i in range(Q):
    cnt = start_cnt
    for j in range(start_j, N):
        if sX[i] > sA[j]:
            cnt += 1
        else:
            counts.update(
                {
                    sX[i]: cnt
                }
            )
            start_j = j
            start_cnt = cnt
            break

# print(counts)

for i in range(Q):
    print(all_count - counts[x[i]])
