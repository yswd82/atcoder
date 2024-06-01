# N = int(input())
# N, M = map(int, input().split())

# A = list(map(int, input().split()))

# B = []
# for i in range(N):
#     B.append(int(input()))

# S = []
# for i in range(N):
#     S.append(input())

# ans = False
# print('Yes') if ans else print('No')
S1 = input()
S2 = input()

s1cnt = sum([1 for s in S1 if s == '#'])
s2cnt = sum([1 for s in S2 if s == '#'])

if s1cnt + s2cnt in (0,1,3,4):
    print('Yes')
else:
    if S1[0] == S2[0] == '#' or S1[1] == S2[1] == '#' or S1[0] == S1[1] == '#' or S2[0] == S2[1] == '#':
        print('Yes')
    else:
        print('No')

