N, Q = map(int, input().split())

# 前にどの電車がいるか
F = [None] * (N+1)
# 後ろにどの電車がいるか
R = [None] * (N+1)

ans = []

for q in range(Q):
    query = list(input().split())

    if query[0] == '1':
        R[int(query[1])] = int(query[2])
        F[int(query[2])] = int(query[1])

    elif query[0] == '2':
        R[int(query[1])] = None
        F[int(query[2])] = None

    elif query[0] == '3':
        current = int(query[1])

        trains = []

        while True:
            # print('C', current)
            # print('F', F)
            # print('R', R)
            if F[current]:
                current = F[current]

            else:
                trains.append(current)

                while R[current]:
                    trains.append(R[current])
                    current = R[current]

                break

        ans.append([len(trains)] + trains)

        # print(len(trains), trains)

# print(ans)
for a in ans:
    s = ' '.join(list(map(str, a)))
    print(s)
