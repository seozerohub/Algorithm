from collections import deque

n,k = map(int, input().split())
dlist = []
alist = []
for i in range(1,n+1):
    dlist.append(i)
deque = deque(dlist)

for i in range(n):
    for j in range(k-1):
        deque.append(deque.popleft())
    alist.append(deque.popleft())

print("<", end='')
for i in range(len(alist)-1):
    print(alist[i],end=', ')
print(alist[len(alist)-1], end='')
print(">")