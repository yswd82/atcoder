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

N, M = map(int, input().split())

A = [0] * M
B = [0] * M

for i in range(M):
    A[i], B[i] = map(int, input().split())

# 最初は全員トップの可能性がある
top = [n+1 for n in range(N)]

# トップでない人を削除する
for i in range(M):
    try:
        top.remove(B[i])
    except:
        pass

if len(top) == 1:
    print(top[0])
else:
    print(-1)
