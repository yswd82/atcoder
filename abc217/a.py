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
s,t = input().split()
d1 = [s,t]
d2 = sorted(d1)
if d1==d2:
    print('Yes')
else:
    print('No')