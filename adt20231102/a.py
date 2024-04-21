import math

s = input()
n = len(set(list(s)))
ans = math.factorial(n)

if ans == 3:
    print(6)
elif ans == 2:
    print(3)
else:
    print(1)
