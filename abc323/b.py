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
S = [None] * N
for i in range(N):
    S[i] = input()


wins = [0] * N

for i in range(N):
    for j in range(N):
        if S[i][j] == "o":
            wins[i] += 1

wins = [(p, w) for p, w in zip(range(N), wins)]

wins = sorted(wins, key=lambda x: x[0])
wins = sorted(wins, key=lambda x: x[1], reverse=True)

print(*[w[0] + 1 for w in wins])
