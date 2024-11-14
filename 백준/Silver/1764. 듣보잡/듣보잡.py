import sys
input = sys.stdin.readline
a,b = map(int,input().strip().split())
slist = []
for i in range(a+b):
    s = input().strip()
    slist.append(s)
d = dict()
for i in slist:
    if i in d:
        d[i]= d[i]+1
    else:
        d[i]=1

dnew = list(filter(lambda x:x[1]==2, d.items()))
dnew = sorted(dnew,key=lambda x:x[0])
print(len(dnew))
for i in range(len(dnew)):
    print(dnew[i][0])