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
U = [0] * M
V = [0] * M
for i in range(M):
    U[i], V[i] = map(int, input().split())

edge = dict()
for u,v in zip(U,V):
    edge.update({(u-1,v-1):1})

answer = []

for a in range(N):
    for b in range(a,N):
        for c in range(b,N):
            ans = 0
            for x in [(a,b),(b,c),(a,c)]:
                try:
                    ans += edge[x]
                except:
                    pass
                if ans == 3:
                    answer.append((a,b,c))
print(len(answer))