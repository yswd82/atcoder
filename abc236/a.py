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
s=input()
a,b=map(int, input().split())

sl = list(s)

sl[b-1], sl[a-1] = sl[a-1],sl[b-1]
print("".join(sl))