s = "wbwbwwbwbwbw"

W, B = map(int, input().split())


r = (W + B) // 12 + 2

S = "".join([s for i in range(r)])


for p in range(12):
    x = S[p : p + W + B]

    if x.count("w") == W and x.count("b") == B:
        print("Yes")
        exit()
print("No")
