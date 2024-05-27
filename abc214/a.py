
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
for i in range(n):
    if 0 <= i <= 124:
        cnt=4
    elif 125 <= i <= 210:
        cnt=6
    elif 211 <= i <= 213:
        cnt=8
print(cnt)