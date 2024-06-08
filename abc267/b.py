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
s = list(map(int,list(input())))

lines = [
    [s[6]],
    [s[3]],
    [s[1],s[7]],
    [s[0],s[4]],
    [s[2],s[8]],
    [s[5]],
    [s[9]],     
]
ans = False
for i in range(5):
    for j in range(i,6):
        for k in range(j,7):
            if s[0] == 0 and sum(lines[i]) > 0 and sum(lines[j]) == 0 and sum(lines[k]) > 0 and k-i>1:
                # print(i,j,k,'split')
                ans = True
print('Yes') if ans else print('No')
