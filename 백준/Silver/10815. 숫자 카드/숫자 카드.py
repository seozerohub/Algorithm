a = int(input())
alist = list(map(int, input().split()))
b = int(input())
blist = list(map(int, input().split()))
clist = []
alist.sort()

for i in range(b):
    start = 0
    end = a-1
    found = False
    while (start<=end):
        mid = (start+end)//2
        if blist[i]<alist[mid]:
            end = mid-1
        elif blist[i]>alist[mid]:
            start=mid+1
        elif blist[i]==alist[mid]:
            clist.append(1)
            found=True
            break
    if found==False:
        clist.append(0)
print(*clist)