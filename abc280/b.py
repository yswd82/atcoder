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
S = list(map(int, input().split()))
A = [0]*N

for i in range(N):
    if i ==0:
        A[i] = S[i]
    else:
        A[i] = S[i]-S[i-1]
print(*A)

