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

comp_s = S[0]
last_chr = S[0]

for s in S[1:]:
    if s == last_chr:
        pass
    else:
        comp_s += s
        last_chr = s

if (
    comp_s == "A"
    or comp_s == "B"
    or comp_s == "C"
    or comp_s == "AB"
    or comp_s == "AC"
    or comp_s == "BC"
    or comp_s == "ABC"
):
    print("Yes")
else:
    print("No")
