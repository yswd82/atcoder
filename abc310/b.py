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

P = [0] * N
C = [0] * N
F = [[]] * N


for i in range(N):
    tmp = list(map(int, input().split()))

    P[i] = tmp[0]
    C[i] = tmp[1]
    F[i] = tmp[2:]

answers = 0

for i in range(N):
    for j in range(N):
        flg_a, flg_b,flg_c,flg_d= False, False, False,False
        if i == j:
            continue

        if P[i] >= P[j]:
            flg_a = True

        fi = F[i].copy()
        for fj in F[j]:
            try:
                fi.remove(fj)
            except:
                pass
        if len(fi) == 0:
            flg_b = True

        fj = F[j].copy()
        for fi in F[i]:
            try:
                fj.remove(fi)
            except:
                pass
        if len(fj) > 0:
            flg_d = True


        if P[i] > P[j] or flg_d:
            flg_c = True

        # print(f"{i} vs {j} {flg_a} {flg_b} {flg_c}")


        if all([flg_a,flg_b,flg_c]):
            answers += 1

ans = True if answers > 0 else False
print('Yes') if ans else print('No')