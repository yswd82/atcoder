s = input()

s = list(s)

l = len(s)

left = ""
center = ""
right = ""

num = "0123456789"

pos = "left"

for i in range(l):
    if pos == "right" and s[i] not in num:
        right += s[i]
    if pos == "right" and s[i] in num:
        print("No")
        exit()

    if pos == "center" and s[i] in num:
        center += s[i]
    if pos == "center" and s[i] not in num:
        pos = "right"
        right += s[i]

    if pos == "left" and s[i] in num:
        pos = "center"
        center += s[i]
    if pos == "left" and s[i] not in num:
        left += s[i]

if (
    len(left) == 1
    and len(center) == 6
    and 100000 <= int(center) <= 999999
    and len(right) == 1
):
    print("Yes")
else:
    print("No")
