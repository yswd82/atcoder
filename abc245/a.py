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
a,b,c,d=map(int, input().split())
taka = a*3600 + b*60
aoki = c*3600 + d*60 + 1

if taka < aoki:
    print('Takahashi')
else:
    print('Aoki')
