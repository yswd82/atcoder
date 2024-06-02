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
n,a,b = map(int, input().split())

allmap = [[None] * b*n for _ in range(a*n) ]

for i in range(a*n):
    for j in range(b*n):
        if i//a % 2 == 0:
            if j//b % 2 == 0:
                allmap[i][j] = '.'
            else:
                allmap[i][j] = '#'    
        else:
            if j//b % 2 == 0:
                allmap[i][j] = '#'
            else:
                allmap[i][j] = '.'    

for i in range(a*n):
    print("".join(allmap[i]))
