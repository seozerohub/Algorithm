a = int(input())
nlist = []
for i in range(a):
    n = list(map(int, input().split()))
    nlist.append(n)
nlist.sort(key=lambda x: (x[0], x[1]))

for point in nlist:
    print(*point)