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

m_idx = []
f_idx = []

for i in range(N):
    if S[i] == "M":
        m_idx.append(i+1)
    else:
        f_idx.append(i+1)
if len(S) == 1:
    ans = True
elif len(set([m % 2 for m in m_idx])) == 1 and len(set([f % 2 for f in f_idx])) == 1:
    ans = True
else:
    ans = False

print('Yes') if ans else print('No')