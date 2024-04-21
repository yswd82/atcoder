import math

N = int(input())
X, Y = [0] * N, [0] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())

# print(N, X, Y)


farest = [0] * N

for i in range(N):
    min_d = 0
    farest_j = None
    for j in range(N):
        d = math.sqrt(math.pow((X[i] - X[j]), 2) + math.pow((Y[i] - Y[j]), 2))
        if min_d < d:
            min_d = d
            farest_j = j

    farest[i] = farest_j


for i in range(N):
    print(farest[i] + 1)
