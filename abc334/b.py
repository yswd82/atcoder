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

A, M, L, R = map(int, input().split())

L -= A
R -= A

pos_l = L // M
pos_r = R // M

# print(pos_l, pos_r)

ans = pos_r - pos_l
print(ans)
