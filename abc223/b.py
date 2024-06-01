# N = int(input())
# N, M = map(int, input().split())

# A = list(map(int, input().split()))

# B = []
# for i in range(N):
#     B.append(int(input()))

# S = []
# for i in range(N):
#     S.append(input())

# ans = False
# print('Yes') if ans else print('No')
S = input()

def shift(s:str):
    return s[1:] + s[0]

ss = [''] * len(S)
ss[0] = S

for i in range(1, len(S)):
    ss[i] = shift(ss[i-1])
ans1 = sorted(ss)[0]
ans2 = sorted(ss)[-1]
print(ans1)
print(ans2)
