S = input()

res = set()

for i in range(3):
    for j in range(3):
        for k in range(3):
            if i != j and j != k and i != k:
                res.add(S[i]+S[j]+S[k])


print(len(res))
