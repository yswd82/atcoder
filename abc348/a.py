N = input()
n = int(N)

result = ["x" if (i + 1) % 3 == 0 else "o" for i in range(n)]
print("".join(result))
