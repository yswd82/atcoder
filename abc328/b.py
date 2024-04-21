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
D = list(map(int, input().split()))

cnt = 0
for n in range(N):
    for d in range(D[n] + 1):
        if len(set(list(str(n + 1) + str(d)))) == 1:
            cnt += 1

print(cnt)
