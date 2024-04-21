h, w = map(int, input().split())
r, c = map(int, input().split())

r -= 1
c -= 1

cnt = 0
if r - 1 > -1:
    cnt += 1
if r < h - 1:
    cnt += 1
if c - 1 > -1:
    cnt += 1
if c < w - 1:
    cnt += 1
print(cnt)
