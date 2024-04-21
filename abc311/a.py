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
S = input()

a_flg, b_flg, c_flg = False,False,False
for i in range(len(S)):
    if S[i] == "A":
        a_flg = True
    if S[i] == "B":
        b_flg = True
    if S[i] == "C":
        c_flg = True
    
    if all([a_flg, b_flg, c_flg]):
        print(i+1)
        exit()
