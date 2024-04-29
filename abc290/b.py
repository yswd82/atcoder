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
N, K = map(int, input().split())
S = input()
T = ""

cnt = 0

for i in range(N):
    if S[i] == 'o' and cnt < K:
        T += "o"
        cnt+=1
    else:
        T+="x"

print(T)

