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

v,a,b,c=map(int,input().split())

use = [a,b,c]
i=0
while True:
    if use[i] <= v:
        v-=use[i]
        i = (i+1) % 3
    else:
        break
ans=['F','M','T']
print(ans[i])