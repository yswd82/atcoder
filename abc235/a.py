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
abc = input()

a = int(abc[0])
b = int(abc[1])
c = int(abc[2])

ans = (a+b+c)*100+(a+b+c)*10+(a+b+c)

print(ans)