import sys
input = sys.stdin.readline

a = int(input())
nlist = []
for i in range(a):
    n = list(map(int, input().split()))
    nlist.append(n)

nlist.sort(key=lambda x: (x[1], x[0]))

for i in nlist:
    print(*i)