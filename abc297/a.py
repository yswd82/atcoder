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

N,D = map(int, input().split())

T = list(map(int, input().split()))

last = T[0]
for i in range(1, N):
    if (T[i] - last) <= D:
        print(T[i])
        exit()
    else:
        last = T[i]
print(-1)
