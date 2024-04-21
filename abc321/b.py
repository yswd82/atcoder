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

N, X = map(int, input().split())

A = list(map(int, input().split()))


min_score = 101

for score in range(101):
    B = A + [score]
    total = sum(B) - max(B) - min(B)

    if total >= X:
        min_score = min(min_score, score)

if min_score > 100:
    min_score = -1

print(min_score)
