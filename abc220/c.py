N = int(input())
A = list(map(int, input().split()))
X = int(input())

tA = sum(A)

d = X % tA

s = 0
for i in range(N):
    s += A[i]

    if s > d:
        print(X // tA * N + i + 1)
        exit()
