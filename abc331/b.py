N, S, M, L = map(int, input().split())

p = 10000 * (N // 6 + 1)

for i in range(N // 6 + 2):
    for j in range(N // 8 + 2):
        for k in range(N // 12 + 2):
            if i * 6 + j * 8 + k * 12 >= N:
                p = min(p, i * S + j * M + k * L)

print(p)
