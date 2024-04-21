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

A = sorted(A)

last_a = A[0]
for a in A[1:]:
    if a - last_a != 1:
        print(last_a+1)
        exit()
    else:
        last_a = a