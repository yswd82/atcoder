n = int(input())
a = list(map(int, input().split()))
b = []
l = 0

for i in range(n):
    b.append(a[i])
    l += 1

    while l > 1:
        if b[-1] == b[-2]:
            b[-2] += 1
            del b[-1]
            # b = b[:-2] + [d]
            l -= 1
        else:
            break

print(l)