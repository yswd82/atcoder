N = int(input())
A = list(map(int, input().split()))

DIV = 998244353

nums = []
for i in range(N):
    nums.append([])
    for j in range(10):
        nums[i].append([])
        nums[i][j] = 0

# 最初の回にある数字の数
nums[0][A[0]] = 1

for i in range(1, N):
    for m in range(10):
        f = (m + A[i]) % 10
        g = (m * A[i]) % 10
        nums[i][f] += nums[i-1][m]
        nums[i][g] += nums[i-1][m]

        nums[i][f] %= DIV
        nums[i][g] %= DIV

for a in nums[N-1]:
    print(a)
