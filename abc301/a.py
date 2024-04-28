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
S = input()

wins = (N +2 - 1) // 2

a = 0
t = 0

for i in range(N):
    if S[i] == "A":
        a+=1
        if a == wins:
            ans = "A"
            print(ans)
            exit()
    if S[i] == "T":
        t+=1
        if t == wins:
            ans = "T"
            print(ans)
            exit()

