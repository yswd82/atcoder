X = input()
N = int(input())
S = []
for i in range(N):
    S.append(input())

words = 'abcdefghijklmnopqrstuvwxyz'

decoder = {}
encoder = {}

for x,w in zip(X, words):
    decoder.update(
        {x:w}
    )
    encoder.update(
        {w:x}
    )

S_decode = []

for s in S:
    l = list(s)
    l = map(lambda x: decoder[x], l)
    S_decode.append(''.join(l))

res = sorted(S_decode)

for r in res:
    l = list(r)
    l = map(lambda x: encoder[x], l)
    print(''.join(l))