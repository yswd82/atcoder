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

s = input()

x,y = s.split('.')
y= int(y)


if 0<=y<=2:
    print(x+'-')
elif 3<=y<=6:
    print(x)
elif 7<=y<=9:
    print(x+'+')