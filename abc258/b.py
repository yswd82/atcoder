# N = int(input())
# N, M = map(int, input().split())
#
# A = list(map(int, input().split()))
#
# B = []
# for i in range(N):
#     B.append(int(input()))
#
# S = []
# for i in range(N):
#     S.append(input())
#
# ans = False
# print('Yes') if ans else print('No')
n=int(input())
a=[None]*n
for i in range(n):
    a[i] = list(map(int,list(input())))

sumss = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        sums = [0] * 10
        for k in range(n):
            sums[6] += a[i][(j+k)%n]*(10**(n-k-1))
            sums[4] += a[i][(j-k)%n]*(10**(n-k-1))
            sums[2] += a[(i+k)%n][j]*(10**(n-k-1))
            sums[8] += a[(i-k)%n][j]*(10**(n-k-1))

            sums[7] += a[(i-k)%n][(j-k)%n]*(10**(n-k-1))
            sums[9] += a[(i-k)%n][(j+k)%n]*(10**(n-k-1))
            sums[1] += a[(i+k)%n][(j-k)%n]*(10**(n-k-1))
            sums[3] += a[(i+k)%n][(j+k)%n]*(10**(n-k-1))
        sumss[i][j] = max(sums)

summax = 0
for i in range(n):
    summax = max(summax, max(sumss[i]))
print(summax)
