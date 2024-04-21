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

C = [0] * N
A = [[0] * N for i in range(N)]

for i in range(N):
    C[i] = int(input())
    A[i] = list(map(int, input().split()))
X = int(input())

me = [38] * N

for i in range(N):
    if X in A[i]:
        me[i] = C[i]

min_me = min(me)

if min_me == 38:
    print(0)
    exit()

ans = []
for i in range(N):
    if me[i] == min_me:
        ans.append(i+1)

ans = sorted(ans)
print(len(ans))
print(*ans)
