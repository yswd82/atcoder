# N = int(input())
# N, M = map(int, input().split())
#
# A = list(map(int, input().split()))
#
# B = []
# for i in range(N):
#     B.append(int(input()))
#
S = input()
# S = []
# for i in range(N):
#     S.append(input())
#
ls = S.lower()
us = S.upper()

l_matches = 0
u_matches = 0
l_ext = False
u_ext = False

sset = set(S)

ans = False

if len(sset) < len(S):
    ans = False
else:

    for s,_ls,_us in zip(S,ls,us):
        if s == _ls:
            l_matches += 1
            l_ext = True

        if s == _us:
            u_matches += 1
            u_ext = True

if l_matches > 0 and u_matches > 0:
    ans = True


print( 'Yes' if ans else 'No')