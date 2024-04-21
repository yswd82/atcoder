N, M = map(int, input().split())

B = []
for n in range(N):
    B.append(list(map(int, input().split())))

# print(B)

# 前行との差が常に7であること
# 7で割った商がすべて同じであること
if N == 1 and M == 1:
    print('Yes')
    exit()
elif N == 1:
    for j in range(M):
        if j > 0:
            if (B[0][j-1]-1) % 7 >= (B[0][j]-1) % 7:
                print('No')
                exit()

elif M == 1:
    for i in range(N):
        if i > 0:
            if B[i][0] - B[i-1][0] != 7:
                print('No')
                exit()
else:
    for i in range(N):
        if i > 0:
            for j in range(M):
                if j > 0:
                    if (B[i][j-1]-1) % 7 >= (B[i][j]-1) % 7:
                        print('No')
                        exit()
            for j in range(M):
                if B[i][j] - B[i-1][j] != 7:
                    print('No')
                    exit()


print('Yes')
