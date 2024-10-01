n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))

nlist.sort()

for i in range(m):
    start = 0
    end = n-1
    found = False

    if mlist[i] > nlist[end] or mlist[i] < nlist[start]:
        print(0)
    else:
            while (start <= end):
                mid = (start + end) // 2
                if mlist[i]>nlist[mid]:
                    start = mid+1
                elif mlist[i] < nlist[mid]:
                    end = mid-1
                else:
                    print(1)
                    found = True
                    break
            if not found:
                print(0)