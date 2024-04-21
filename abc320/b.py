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
S = input()


def is_kaibun(string):
    ans = True
    for i in range(len(string) // 2):
        if string[i] == string[-1 - i]:
            pass
        else:
            ans = False
            break
    return ans


max_len = 1

for i in range(len(S)):
    for l in range(1, len(S) - i + 1):
        if is_kaibun(S[i : min(i + l, len(S))]):
            max_len = max(max_len, l)

print(max_len)
