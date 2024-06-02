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
a,b,c,x = map(int,input().split())
if x <= a:
    ans = 1
elif a+1 <= x <= b:
    ans = c / (b-a)
else:
    ans = 0
print(ans)