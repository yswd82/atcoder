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
a = list(map(int, input().split()))

last = None




chain = [(i+1,i+2) for i in range(N) if i+1 in a]

print(chain)
# res = []
# last = chain[0]
# for i in range(len(chain)):
#     if chain[i][0] - 1 == chain[i-1][0] and chain[i][1] - 1 == chain[i-1][1]:
#         pass
#     else:
#         sorted(chain[i-1])
        

