# N = int(input())
# N, M = map(int, input().split())

P = list(map(int, input().split()))

# B = []
# for i in range(N):
#     B.append(int(input()))

# S = []
# for i in range(N):
#     S.append(input())

# ans = False
# print('Yes') if ans else print('No')


S = [chr(65+32+p-1) for p in P]
print(''.join(S))