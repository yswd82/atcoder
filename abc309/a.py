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


A,B = map(int, input().split())

if A == 1:
    ans = [2]
elif A== 2:
    ans = [1,3]
elif A== 3:
    ans = [2]
elif A== 4:
    ans = [5]
elif A== 5:
    ans = [4,6]
elif A== 6:
    ans = [5]
elif A== 7:
    ans = [8]
elif A== 8:
    ans = [7,9]
elif A== 9:
    ans = [8]

answer = B in ans
print('Yes') if answer else print('No')

