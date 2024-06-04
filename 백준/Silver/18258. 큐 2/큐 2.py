import sys
from collections import deque
input = sys.stdin.readline

a = int(input().rstrip())
queue = deque([])

for i in range(a):
    s = input().rstrip()
    if s == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif s=='front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif s=='empty':
        if queue:
            print(0)
        else:
            print(1)
    elif s== 'size':
        print(len(queue))
    elif s== 'pop':
        if queue:
            print(queue[0])
            queue.popleft()
        else:
            print(-1)
    else:
        queue.append(s[5::])