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

called = [0] * N

for i in range(N):
    if not called[i]:
        called[A[i] -1] = 1

uncalled = [i+1 for i in range(N) if called[i] == 0]
print(len(uncalled))
print(*uncalled)



