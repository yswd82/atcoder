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
p,q = input().split()

dis = [3,1,4,1,5,9]
dis_sum = [None] * (len(dis)+1)

dis_sum[0] = 0
for i in range(1, len(dis)+1):
    dis_sum[i] = dis_sum[i-1] + dis[i-1]

char = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
}

print(abs(dis_sum[char[q]] - dis_sum[char[p]]))