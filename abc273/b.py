import decimal
from decimal import ROUND_HALF_UP

X,K = map(int, input().split())

X = decimal.Decimal(X)

for k in range(K):
    
    X = X / (10 ** (k+1))
    X = X.quantize(decimal.Decimal('0'), ROUND_HALF_UP )
    X = X * (10 ** (k+1))
print(int(X))
