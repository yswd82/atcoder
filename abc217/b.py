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
contests =  ['ABC' , 'ARC' , 'AGC' , 'AHC']
s1 = input()
s2 = input()
s3 = input()

contests.remove(s1)
contests.remove(s2)
contests.remove(s3)

print(contests[0])
