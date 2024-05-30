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
n = int(input())
s = [0]*n
t = [0]*n

for i in range(n):
    s[i], t[i] = input().split()

for i in range(n):
    for j in range(n):
        if i!=j and s[i] == s[j] and t[i] == t[j]:
            ans = True
            print('Yes')
            exit()
print('No')