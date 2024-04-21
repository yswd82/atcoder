S = input()


for p in range(len(S)):
    # <
    if S[p] == "<":
        for p2 in range(p, len(S)):
            # >
            if S[p2] == ">":
                # 中間
                e = S[p + 1 : p2]

                if e.count("=") == len(e):
                    if e.count("=") + 2 == len(S):
                        print("Yes")
                        exit()
print("No")
