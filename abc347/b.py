s = input()

result = 0

for l in range(1, len(s) + 1):
    x = set()
    for i in range(len(s) - l + 1):
        # print(s[i : i + l - 1])
        x.add(s[i : i + l])

    result += len(x)
    # print(f"long{l} cnt={len(x)} total={result}")

print(result)
