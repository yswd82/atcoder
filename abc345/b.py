import math

X = int(input())

# 末尾の文字
r = str(X)[-1]

if abs(X) <= 10:
    res = math.ceil(X / 10)
else:
    if r == "0":
        res = str(X)[:-1]
    else:
        y = str(X)[:-1]

        if y == "":
            res = 1
        else:
            if str(X)[0] == "-":
                res = int(y)
            else:
                res = int(y) + 1

print(int(res))
