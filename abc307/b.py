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

S = [None] * N
for i in range(N):
    S[i] = input()


def is_kaibun(v:str):
    m = len(v)
    return all([ v[i] == v[-i-1] for i in range(m)])

ans =False
for i in range(N):
    for j in range(N):
        if i != j:
            s = S[i] + S[j]
            if is_kaibun(s):
                ans = True
                break
print('Yes') if ans else print('No')

