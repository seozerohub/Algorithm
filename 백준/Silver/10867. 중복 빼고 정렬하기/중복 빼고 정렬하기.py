a = int(input())
nlist = list(map(int, input().split()))
nlist = set(nlist)
nlist = list(nlist)
nlist.sort()
for i in range(1):
    print(*nlist)