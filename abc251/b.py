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
n,w = map(int, input().split())
a = list(map(int, input().split()))

from itertools import combinations
ansset = set()
for i in range(3):
    comb = list(combinations(a,i+1))
    for c in comb:
      seisu = sum(c)
      if seisu <= w:
          ansset.add(seisu)
print(len(ansset))

