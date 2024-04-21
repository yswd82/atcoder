# N = int(input())
# A = list(map(int, input().split()))
# B = []
# for i in range(N):
#     B.append(int(input()))
S = input()
T = input()

s_ord = [ord(s) for s in S]
t_ord = [ord(t) for t in T]

for k in range(27):
    ss_ord = [s + k if s + k <= 122 else s + k - 26 for s in s_ord]

    if ss_ord == t_ord:
        print('Yes')
        exit()

print('No')

# stdiff = [s-t for s, t in zip(s_ord, t_ord)]

# if len(set(stdiff)) == 1:
#     print('Yes')
# else:
#     print('No')
