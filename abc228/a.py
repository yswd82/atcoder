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
s,t,x = map(int, input().split())

if t <= s:
    t += 24

if s <= x < t or s<= x+24 < t:
    print('Yes')
else:
    print('No')
