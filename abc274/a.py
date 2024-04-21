from decimal import Decimal, ROUND_HALF_UP

A,B = map(int, input().split())

x = Decimal(B /A).quantize(Decimal('0.001'), ROUND_HALF_UP)

print(x)