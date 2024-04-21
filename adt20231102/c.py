n = 8
r = 8
c = 1

cols = "abcdefgh"

s = []

for i in range(8):
    s.append(input())

for _ in s:
    if "*" in list(_):
        c = list(_).index("*")

        print(cols[c] + str(r))
        exit

    r -= 1
