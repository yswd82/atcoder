# N = int(input())


# A = list(map(int, input().split()))

# B = []
# for i in range(N):
#     B.append(int(input()))

# S = []
# for i in range(N):
#     S.append(input())

# ans = False
# print('Yes') if ans else print('No')

s,t = map(int, input().split())
ans = set()
for a in range(101):
    for b in range(101):
        for c in range(101):
            if a+b+c <= s and a*b*c <= t:
                ans.add((a,b,c))


print(len(ans))