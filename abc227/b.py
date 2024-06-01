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
n = int(input())
S = list(map(int, input().split()))

def menseki(a,b):
    return 4*a*b + 3*a + 3*b

sl = []

for i in range(1,1001):
    for j in range(1,1001):
        s = menseki(i,j)
        if 1000 < s:
            continue
    
        sl.append(s)

ans = [_ for _ in S if _ not in sl]

print(len(ans))