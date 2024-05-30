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

# A_ = sorted(A, reverse=True)

# print(A.index(A_[1]) + 1)
s = input()
t = input()
s = list(s)
t = list(t)

cnt = 0
for i in range(len(s)-1):
    if t[i] == s[i+1] and t[i+1] == s[i]:
        cnt += 1

if 2 <= cnt:
    print('No')
else:
    print('Yes')