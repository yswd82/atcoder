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
n=int(input())
p=list(map(int,input().split()))
p=[0,0]+p


crr = n
gen = 0

while crr != 1:
    # print(crr,gen)
    
    crr = p[crr]
    gen += 1

print(gen)
