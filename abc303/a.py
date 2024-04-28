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
T = input()

pat = [("1", "l"), ("0", "o")]

ans = True
for s,t in zip(S,T):
    if s != t:
        if s in ["1","l","0","o"]:
            for p in pat:
                if s == p[0]:
                    if t == p[1]:
                        pass
                    else:
                        ans = False

                if s == p[1]:
                    if t == p[0]:
                        pass
                    else:
                        ans = False
        else:
            ans = False

print('Yes') if ans else print('No')