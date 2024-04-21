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

M = int(input())
D = list(map(int, input().split()))

allday = []

for m in range(M):
    for d in range(D[m]):
        allday.append((m,d))

idx = len(allday) // 2

res = allday[idx]

print(res[0]+1, res[1]+1)
