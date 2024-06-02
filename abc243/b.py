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
b = list(map(int, input().split()))

cnt1=0
cnt2=0

for i in range(n):
    for j in range(n):
        if i==j and a[i] == b[j]:
            cnt1+=1
        if i!=j and a[i] == b[j]:
            cnt2+=1
print(cnt1)
print(cnt2)