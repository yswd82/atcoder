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

N = input()

ans = True

last_chr = N[0]
for i in range(1, len(N)):
    if int(N[i]) < int(last_chr):
        last_chr = N[i]
    else:
        ans = False
        break

print("Yes") if ans else print("No")
