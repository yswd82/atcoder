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
Q = int(input())
query = []
A = []
for i in range(Q):
    query.append(list(map(int, input().split())))

for i in range(Q):
    if query[i][0] == 1:
        A.append(query[i][1])
    if query[i][0] == 2:
        print(A[int(query[i][1]) * -1])
