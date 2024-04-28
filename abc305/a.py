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
N = int(input())

prev_ = (N // 5)*5
next_ = (N // 5+1)*5

if N - prev_ < next_ - N:
    print(prev_)
else:
    print(next_)


