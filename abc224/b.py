# N = int(input())
# N, M = map(int, input().split())

# A = list(map(int, input().split()))

# B = []
# for i in range(N):
#     B.append(int(input()))

# S = []
# for i in range(N):
#     S.append(input())

# ans = False
# print('Yes') if ans else print('No')
h,w= map(int, input().split())
a = [None] * h

for i in range(h):
    a[i] = list(map(int, input().split()))

for i1 in range(h):
    for i2 in range(i1,h):
        for j1 in range(w):
            for j2 in range(j1,w):
                if a[i1][j1] + a[i2][j2] <= a[i2][j1] + a[i1][j2]:
                    pass
                else:
                    print('No')
                    exit()

print('Yes')