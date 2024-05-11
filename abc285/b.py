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

N:int = int(input())
S:str = input()

for i in range(1, N):
    l_max = 0
    for l in range(N-i):
        if all([S[k] != S[k+i] for k in range(l)]):
            l_max = max(l_max, l)

    print(l_max)
