# N = int(input())
# A = list(map(int, input().split()))
# B = []
# for i in range(N):
#     B.append(int(input()))
import pprint
H, W = map(int, input().split())
C = []
for i in range(H):
    l = list(input())
    C.append(l)

step = []
for i in range(H):
    step.append([])
    for j in range(W):
        step[i].append(0)


step[0][0] = 1

maxstep = 1

for i in range(H):
    for j in range(W):
        if C[i][j] == '.':
            if j > 0:
                if C[i][j-1] == '.':
                    if step[i][j] <= step[i][j-1] and step[i][j-1] > 0:
                        step[i][j] = step[i][j-1] + 1
            if i > 0:
                if C[i-1][j] == '.':
                    if step[i][j] <= step[i-1][j] and step[i-1][j] > 0:
                        step[i][j] = step[i-1][j] + 1
            if i > 0 and j > 0:
                # 2方向から来れるとき
                if C[i-1][j] == '.' and C[i][j-1] == '.':
                    if step[i-1][j] > 0 and step[i][j-1] > 0:
                        step[i][j] = max(step[i-1][j], step[i][j-1]) + 1

                elif C[i-1][j] == '.' and C[i][j-1] == '#':
                    if step[i][j] <= step[i-1][j] and step[i-1][j] > 0:
                        step[i][j] = step[i-1][j] + 1

                elif C[i-1][j] == '#' and C[i][j-1] == '.':
                    if step[i][j] <= step[i][j-1] and step[i][j-1] > 0:
                        step[i][j] = step[i][j-1] + 1

            maxstep = max(maxstep, step[i][j])

print(maxstep)
