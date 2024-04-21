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
takcode_ul = [
    "###.",
    "###.",
    "###.",
    "...."
]
takcode_br = [
    "....",
    ".###",
    ".###",
    ".###"
]

N, M = map(int, input().split())
S = [None] * N

for i in range(N):
    S[i] = input()

ans = []
for i in range(N-9+1):
    for j in range(M-9+1):
        ul = []
        br = []
        for h in range(4):
           ul.append(S[i+h][j:j+4])
           br.append(S[i+h+5][j+5:j+5+4])

        if ul == takcode_ul and br == takcode_br:
            ans.append((i+1,j+1))

for a in ans:
    print(*a)

