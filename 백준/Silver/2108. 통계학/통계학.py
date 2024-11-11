import sys
input = sys.stdin.readline
a = int(input())
nlist = []
for i in range(a):
    n = float(input())
    nlist.append(n)

t = (sum(nlist)/a)
t = f"{t:.0f}"
print(int(t))
nlist.sort()
print(int(nlist[a//2]))
d = dict()
for i in nlist:
    if i in d:
        d[i]= d[i]+1
    else:
        d[i]=1
newd = sorted(d.items(), key=lambda x:(-x[1],x[0]))
if len(newd)>1 and newd[0][1]== newd[1][1]:
    print(int(newd[1][0]))
else:
    print(int(newd[0][0]))
print(int(max(nlist)-min(nlist)))