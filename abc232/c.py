import collections
N, M = map(int, input().split())
# A = list(map(int, input().split()))
A = []
B = []
for i in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

C = []
D = []
for i in range(M):
    c, d = map(int, input().split())
    C.append(c)
    D.append(d)

taka_ball = [0] * N
aoki_ball = [0] * N


# すべてのたまについて、玉につながっているひもの数を数える
for j in range(M):
    taka_ball[A[j]-1] += 1
    taka_ball[B[j]-1] += 1

    aoki_ball[C[j]-1] += 1
    aoki_ball[D[j]-1] += 1

taka_c = collections.Counter(taka_ball)
aoki_c = collections.Counter(aoki_ball)

print(taka_c, aoki_c)

for i in range(N):
    taka_c[i]
    # print(taka_ball, aoki_ball)


if taka_c == aoki_c:
    print('Yes')
else:
    print('No')
