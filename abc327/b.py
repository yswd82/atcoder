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

# import collections

# d = collections.defaultdict()
# d.setdefault(-1)

B = int(input())

d = {}

for a in range(1, 18):
    d.update({a**a: a})

ans = d.get(B)

if ans:
    print(ans)
else:
    print(-1)
