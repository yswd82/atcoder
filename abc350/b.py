N,Q = map(int, input().split())

T = list(map(int, input().split()))

tooth = [1] * N

for i in range(Q):
    if tooth[T[i]-1] == 1:
        tooth[T[i]-1] = 0
    else:
        tooth[T[i]-1] = 1

print(sum(tooth))
