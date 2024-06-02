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
base = [0] * 4
n = int(input())
a = list(map(int, input().split()))
p=0
for i in range(n):
    base[0] = 1

    addlist = [0] * a[i]
    base = addlist + base

    p+=sum(base[4:])

    base = base[:4]

print(p)