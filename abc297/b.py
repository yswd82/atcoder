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
S = input()

b_idx = []
r_idx = []

for i in range(8):
    if S[i] == "B":
        b_idx.append(i+1)
    if S[i] == "R":
        r_idx.append(i+1)
    if S[i] == "K":
        k_idx = i+1

if sum([b % 2 for b in b_idx]) == 1 and min(r_idx) < k_idx < max(r_idx):
    ans = True
else:
    ans = False

print('Yes') if ans else print('No')
