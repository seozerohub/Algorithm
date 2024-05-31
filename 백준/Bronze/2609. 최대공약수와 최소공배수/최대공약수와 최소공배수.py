a,b = map(int, input().split())
nlist = []
for i in range(1, min(a,b)+1):
    if a%i==0 and b%i==0:
        nlist.append(i)
r = max(nlist)
a = a/r
b = b/r
print(r)
print(int(r*a*b))