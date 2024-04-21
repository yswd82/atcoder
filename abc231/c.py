N, Q = map(int, input().split())

A = list(map(int, input().split()))
x = []
for i in range(Q):
    x.append(int(input()))

sortedA = sorted(A)
all_cnt = len(sortedA)

for i in range(Q):
    l = 0
    r = all_cnt-1
    # mid = (l+r)//2

    while l <= r:
        mid = (l+r)//2
        midv = sortedA[mid]

        if x[i] < midv:
            r = mid-1
        elif x[i] > midv:
            l = mid+1
        elif x[i] == midv:
            l = mid
            break

        # print(l, mid, r, x[i], midv)
        if l == mid or mid == r:
            break

    # print('ans', sortedA[l], sortedA[mid], sortedA[r])
    print(all_cnt - l)
