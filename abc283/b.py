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
A = list(map(int, input().split()))
Q = int(input())
query = [0] * Q
for i in range(Q):
    query[i] = input().split()

for i in range(Q):
    k = int(query[i][1])
    if query[i][0] == "1":
        x = int(query[i][2])
        A[k-1] = x
    if query[i][0] == "2":
        print(A[k-1])

