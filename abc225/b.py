N = int(input())
A = [0] * N
B = [0] * N

for i in range(N-1):
    a, b = map(int, input().split())

    A[i] = a-1
    B[i] = b-1

    # print(A[i], B[i])

top = [0] * N

for i in range(N-1):
    top[A[i]] += 1
    top[B[i]] += 1

# print(top)

if (N-1) in top:
    print('Yes')
else:
    print('No')
