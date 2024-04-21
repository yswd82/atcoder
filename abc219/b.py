S1 = input()
S2 = input()
S3 = input()
T = input()

s = ''

for t in T:
    if t == '1':
        s += S1
    elif t == '2':
        s += S2
    elif t == '3':
        s += S3

print(s)