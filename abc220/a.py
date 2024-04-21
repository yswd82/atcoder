A, B, C = map(int, input().split())

mul = 1

while True:
    if C * mul > B:
        print(-1)
        exit()
    elif A <= C * mul <= B:
        print(C*mul)
        exit()

    mul += 1
