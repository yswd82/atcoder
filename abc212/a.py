A,B = map(int, input().split())
if 0 < A and B == 0:
    ans = 'Gold'
elif A==0 and 0 < B:
    ans = 'Silver'
elif 0 < A and 0 < B:
    ans = 'Alloy'

print(ans)