import sys
input = sys.stdin.readline
m = int(input().strip())
s = set()
for i in range(m):
    ab = input().strip().split()
    if len(ab)==2:
        a = ab[0]
        b = int(ab[1])
    else:
        a = ab[0]
    if a == 'add':
        s.add(b)
    elif a== 'check':
        if b in s:
            print(1)
        else:
            print(0)
    elif a == 'remove':
        s.discard(b)
    elif a == 'toggle':
        if b in s:
            s.discard(b)
        else:
            s.add(b)
    elif a == 'all':
        s = set(range(1, 21))
    elif a == 'empty':
        s = set()