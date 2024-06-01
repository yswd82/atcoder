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
n,k,a = map(int, input().split())

ans = (a + k - 1) % n

if ans == 0:
    ans = n
print(ans)
