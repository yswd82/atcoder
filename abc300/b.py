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

H,W = map(int, input().split())
A = [None] * H
B = [None] * H

for i in range(H):
    A[i] = list(input())
for i in range(H):
    B[i] = list(input())

def shift_s(val):
    res = []
    for i in range(1, H):
        res.append(val[i])
    res.append(val[0])
    return res

def shift_t(val):
    res = []
    for i in range(H):
        li = val[i][1:]
        li.extend(val[i][0])

        res.append(li)
    return res

def equal_map(val1, val2):
    ans = True
    for i in range(H):
        for j in range(W):
            if val1[i][j] != val2[i][j]:
                ans = False
    return ans

def print_map(val):
    for i in range(H):
        print(val[i])



for i in range(H):
    B = shift_s(B)
    for j in range(W):
        B = shift_t(B)

        if equal_map(A, B):
            print("Yes")
            exit()

print("No")

