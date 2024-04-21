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

ans = True
for i in range(2, 17, 2):
    if S[i - 1] != "0":
        ans = False
        break

print("Yes") if ans else print("No")
