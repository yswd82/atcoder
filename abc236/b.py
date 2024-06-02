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
n=int(input())
a = list(map(int, input().split()))

cards = [0] * n

for _ in a:
    cards[_-1] += 1

for i,c in enumerate(cards):
    if c == 3:
        print(i+1)
        exit()