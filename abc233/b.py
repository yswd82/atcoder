L, R = map(int, input().split())
S = input()
# A = list(map(int, input().split()))
# B = []
# for i in range(N):
#     B.append(int(input()))
# ans = False
# print('Yes') if ans else print('No')

S = list(S)


if L > 1:
    l = ''.join(S[0:L-1])
else:
    l = ''

m = ''.join(S[L-1:R])
m = ''.join(reversed(m))

if R < len(S):
    r = ''.join(S[R:])
else:
    r = ''

print(l+m+r)
