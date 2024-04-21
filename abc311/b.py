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

N, D = map(int, input().split())

S = [None] * N

for i in range(N):
    S[i] = input()

seq = 0
max_seq = 0

for d in range(D):
    if all([S[n][d] == "o" for n in range(N)]):
        seq += 1
        max_seq = max(max_seq, seq)
    else:
        seq = 0

print(max_seq)
