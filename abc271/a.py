N = int(input())

binn = hex(N)[2:]

if len(binn) % 2 == 1:
    binn = "0" + binn
print(binn.upper())

