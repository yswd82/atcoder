X = int(input())

if X >= 90:
    res = 'expert'
elif 70 <= X < 90:
    res = 90 - X
elif 40 <= X < 70:
    res = 70 - X
elif 0 <= X < 40:
    res = 40 - X

print(res)
