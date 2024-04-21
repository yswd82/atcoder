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
X = [None] * N
Y = [None] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())

if sum(X) > sum(Y):
    print("Takahashi")
elif sum(X) < sum(Y):
    print("Aoki")
else:
    print("Draw")
