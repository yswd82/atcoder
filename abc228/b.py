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

n,x = map(int, input().split())
a = list(map(int, input().split()))

known = set()
known.add(x)
next = x

checked = set()

while True:
    if next -1 in checked:
        break

    checked.add(next-1)
    known.add(next)

    next = a[next-1]

print(len(known))