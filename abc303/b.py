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

N, M = map(int, input().split())

a = [ [0] * N for i in range(M)]

for i in range(M):
    a[i] = list(map(int, input().split()))


all_pat = set()

for i in range(N):
    for j in range(N):
        if i < j:
            all_pat.add((i,j))

# print(all_pat)

for _a in a:
    for j in range(N):
        prev_ = max(j-1, 0)
        next_ = min(N-1, j+1)

        if _a[j] != _a[prev_]:
            try:
                all_pat.remove((_a[j]-1, _a[prev_]-1))
                all_pat.remove((_a[prev_]-1,_a[j]-1))
            except:
                pass
        if _a[j] != _a[next_]:
            try:
                all_pat.remove((_a[j]-1, _a[next_]-1))
                all_pat.remove((_a[next_]-1, _a[j]-1))
            except:
                pass

print(len(all_pat))