n, k = map(int, input().split())
a = list(map(int, input().split()))

result = []

for i in range(n):
    if a[i] % k == 0:
        result.append(str(a[i] // k))

# print(result)

print(" ".join(result))
