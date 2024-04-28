S = input()
s1 = S[:3]
s2 = S[3:]

if s1 == 'ABC' and 1 <= int(s2) <= 349 and int(s2) != 316:
    print("Yes")
else:
    print("No")
