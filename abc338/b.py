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
import collections

S = input()

c = collections.Counter(S)

li = c.most_common()
li = sorted(li, key=lambda x: x[0])
li = sorted(li, key=lambda x: x[1], reverse=True)
print(li[0][0])
