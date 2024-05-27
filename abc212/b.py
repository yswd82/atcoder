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
s = list(map(int, list(input())))

ans = False
if s[0] == s[1] == s[2] == s[3]:
    ans = True

if all([(s[i] + 1)%10 == s[i+1] for i in range(3)]):
    ans = True

print('Weak') if ans else print('Strong')