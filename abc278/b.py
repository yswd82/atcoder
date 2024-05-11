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
H, M = map(int, input().split())

while True:
    if H < 10:
        lu = 0
        ld = H
    else:
        lu = H // 10
        ld = H % 10

    if M < 10:
        ru = 0
        rd = M
    else:
        ru = M // 10
        rd = M % 10
    
    if 0 <= int(str(lu) + str(ru)) <= 23 and 0<= int(str(ld) + str(rd))<= 59:
        print(H, M)
        exit()
    else:
        M = M + 1
        if M > 59:
            M -= 60
            H += 1
        if H > 23:
            H -= 24 