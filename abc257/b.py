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
n,k,q = map(int, input().split())
a=list(map(int, input().split()))
l=list(map(int, input().split()))

masu = [0] * n
for i in range(k):
    masu[a[i]-1] = 1

for i in range(q):
    cnt=0
    j=0
    while True:
        cnt += masu[j]
        if cnt == l[i]:
            # Li番目のを見つけた
            if j == n-1:
                # 一番右にある
                pass
            else:
                if masu[j+1] == 0:
                    masu[j+1] = 1
                    masu[j] = 0
            break
        j+=1

ans = [i+1 for i in range(n) if masu[i] == 1]
print(*ans)
