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

N = int(input())
S = [0] * N
for i in range(N):
    S[i] = input()
counted = []
ans = True
for s in S:
    if s[0] in ['H' , 'D' , 'C' , 'S'] and s[1] in ['A' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , 'T' , 'J' , 'Q' , 'K' ] and s not in counted:
        counted.append(s)
    else:
        ans = False
print('Yes') if ans else print('No')
