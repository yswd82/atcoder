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

ans = []

last = A[0]
# ans.append(A[0])

for i in range(1, N):
    if last < A[i]:
        li = list(range(last, A[i]))
    if last > A[i]:
        li = list(range(last, A[i], -1))
    last = A[i]
    ans.extend(li)

ans.append(A[N-1])

print(*ans)

