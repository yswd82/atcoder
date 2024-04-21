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

N = int(input())

for n in range(N, 920):
    a, b, c = n // 100, (n - n // 100 * 100) // 10, n % 10

    if a * b == c:
        print(n)
        exit()
