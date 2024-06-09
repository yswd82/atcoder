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

campus = [['#'] * 3**n for i in range(3**n) ]

for i in range(3**n):
    for j in range(3**n):
        for _n in range(n):
            unitsize = 3**(_n+1)
            subunitsize = 3**_n

            if (i//subunitsize) % unitsize == 1 and (j//subunitsize) % unitsize == 1:
                campus[i][j] = '.'
            if n >= 3 and (i//unitsize) % 3 == 1 and (j//unitsize) % 3 == 1:
                campus[i][j] = '.'

for l in campus:
    print(''.join(l))