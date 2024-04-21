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
S = input()

dels = "aeiou"

res = []
for s in S:
    flg = False
    for d in dels:
        if s == d:
            flg = True
    if not flg:
        res.append(s)

print("".join(res))