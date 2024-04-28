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
N,Q = map(int, input().split())
event = [None] * Q

for i in range(Q):
    event[i] = list(map(int, input().split()))

sensyu = [0] * N

for e in event:
    if e[0] == 1:
        sensyu[e[1] - 1] += 1
    if e[0] == 2:
        sensyu[e[1] - 1] += 2
    if e[0] == 3:
        if sensyu[e[1] - 1] >= 2:
            print("Yes")
        else:
            print("No")



