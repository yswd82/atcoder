# N = int(input())
A,B,C,D,E,F,X = map(int, input().split())
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


taka_cnt = X // (A+C)
taka_walk = (taka_cnt * A + min(X % (A+C), A)) * B

aoki_cnt = X // (D+F)
aoki_walk = (aoki_cnt * D + min(X % (D+F), D)) * E

if taka_walk > aoki_walk:
    print('Takahashi')
elif taka_walk < aoki_walk:
    print('Aoki')
elif taka_walk == aoki_walk:
    print('Draw')

# print(taka_walk,aoki_walk)

