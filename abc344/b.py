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

A = []

try:
    while True:
        s = input()
        if s:
            A.append(int(s))
        else:
            break
except:
    pass

for i in range(len(A) - 1, -1, -1):
    print(A[i])
