a, b = map(int,input().split())
nlist = []
for i in range(1,a+1):
    if a%i==0:
        nlist.append(i)

if len(nlist) < b:
    print("0")
else:
    print(nlist[b-1])