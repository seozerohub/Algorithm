a = list(input())
nlist = []
for i in a:
    i = int(i)
    nlist.append(i)

nlist.sort(reverse=True)
for i in nlist:
    print(i, end='')