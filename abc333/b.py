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
T = input()

distance = {
    ("A", "B"): 1,
    ("A", "C"): 2,
    ("A", "D"): 2,
    ("A", "E"): 1,
    ("B", "C"): 1,
    ("B", "D"): 2,
    ("B", "E"): 2,
    ("C", "D"): 1,
    ("C", "E"): 2,
    ("D", "E"): 1,
}

S = sorted(S)
ds = distance[(S[0], S[1])]
T = sorted(T)
dt = distance[(T[0], T[1])]

if ds == dt:
    print("Yes")
else:
    print("No")
