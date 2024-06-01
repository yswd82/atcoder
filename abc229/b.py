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
a,b = input().split()

for i in range(20):
    _a = 0
    try:
        _a = int(a[-1-i])
    except:
        pass

    _b = 0
    try:
        _b = int(b[-1-i])
    except:
        pass

    if _a + _b >= 10:
        print('Hard')
        exit()
print('Easy')



