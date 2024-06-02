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
a = list(map(int, input().split()))
a = sorted(set(a))

ans=0
for i in range(len(a)):
    if ans < a[i]:
        print(ans)
        exit()
    else:
        ans+=1
print(max(a)+1)