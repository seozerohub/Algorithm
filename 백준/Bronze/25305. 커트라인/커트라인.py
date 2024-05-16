a,b = map(int, input().split())
nlist = list(map(int, input().split()))
nlist.sort()
print(nlist[a-b])