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

n = int(input())
l = [None] * n
a = set()
for i in range(n):
    tmp = list(map(int, input().split()))
    l[i] = tmp[0]
    t = tuple(tmp[1:])
    a.add(t)

print(len(a))