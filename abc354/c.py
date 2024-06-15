# N = int(input())
# N, M = map(int, input().split())

# A = list(map(int, input().split()))

# B = []
# for i in range(N):
#     B.append(int(input()))

# S = []
# for i in range(N):
#     S.append(input())

# ans = False
# print('Yes') if ans else print('No')
n = int(input())
from typing import List
from dataclasses import dataclass

@dataclass
class Card:
    i:int
    a:int
    c:int

cards = [Card]*n

for i in range(n):
    _a,_c=map(int,input().split())
    cards[i] = Card(i,_a,_c)

cards = sorted(cards, key=lambda x: x.c)

v=0
s=[]
for card in cards:
    if card.a > v:
        s.append(card.i)
        v=card.a
print(len(s))
print(*sorted([i+1 for i in s]))
