a = int(input())
b = int(input())
nlist = []
# a =3 b=7
for i in range(a,b+1):
    if i==1:
        continue
    p = True
    for j in range(2,i):
        if i%j==0:
            p=False
    if p:
        nlist.append(i)

if nlist == []:
    print(-1)
else:
    print(sum(nlist))
    print(min(nlist))