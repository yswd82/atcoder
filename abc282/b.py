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
S = [0] * N

for i in range(N):
    S[i] = [ 1 if x == 'o' else 0 for x in list(input())]

cnt = 0
for x in range(N-1):
    for y in range(x,N):
        if x != y:
            if all([n | m for n, m in zip(S[x], S[y])]):
                cnt += 1

print(cnt)