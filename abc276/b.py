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
A = [0] * M
B = [0] * M

for i in range(M):
    A[i], B[i] = map(int, input().split())

# 順方向と逆方向のリストを合わせる
road = []
for i in range(M):
    road.append((A[i], B[i]))
    road.append((B[i], A[i]))

# 並べる [0]を接続先の都市、[1]を自都市とする
road = sorted(road)


cnt = [0] * N
connect = [[] for i in range(N)]

for r in road:
    cnt[r[1]-1] += 1
    connect[r[1]-1].append(r[0])

for i in range(N):
    print(cnt[i], *connect[i])
