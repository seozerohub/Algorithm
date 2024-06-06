nlist = list(map(int,input().split()))
p = True
for i in range(len(nlist)-1):
    if nlist[i]<=nlist[i+1]:
        pass
    else:
        p = False
if p:
    print('Good')
else:
    print('Bad')