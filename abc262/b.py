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



def next_edge(n):
    ans = []
    for i in range(M):
        if U[i]==n:
            ans.append(V[i])
    return ans

Z =[ set([i+1]) for i in range(N)]

for i in range(M):
    Z[U[i]-1].add(V[i])
    Z[V[i]-1].add(U[i])
print(Z)
ans = set([tuple(z) for z in Z if len(z) == 3])
print(len(ans))