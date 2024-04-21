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

s = [None] * (N + 1)

for i in range(N + 1):
    if i == 0:
        s[i] = "1"
    elif i == N:
        s[i] = "1"
    else:
        min_j = N
        li = []
        for j in range(1, 10):
            if N % j == 0 and i % (N / j) == 0:
                li.append(j)

        if li:
            s[i] = str(min(li))
        else:
            s[i] = "-"


print("".join(s))
