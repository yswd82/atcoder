# N = int(input())
# N, M = map(int, input().split())
#
# A = list(map(int, input().split()))
#
# B = []
# for i in range(N):
#     B.append(int(input()))
#
# S = []
# for i in range(N):
#     S.append(input())
#
# ans = False
# print('Yes') if ans else print('No')
S = input()
T = input()

for i in range(len(S) - len(T) + 1):
    if S[i:i+len(T)] == T:
        print('Yes')
        exit()
print('No')