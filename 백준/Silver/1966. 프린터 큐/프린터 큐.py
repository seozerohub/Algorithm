from collections import deque
x = int(input())
for i in range(x):
    n, m = map(int, input().split())
    alist = deque(map(int, input().split()))
    nlist = deque(enumerate(alist))
    mlist = deque(enumerate(alist))
    cnt = 0

    while True:
        if nlist[0][1] < max(nlist, key=lambda x: x[1])[1]:
            nlist.append(nlist.popleft())
        else:
            cnt = cnt + 1
            if nlist[0][0] == mlist[m][0]:
                print(cnt)
                break
            else:
                nlist.popleft()
