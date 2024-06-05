import sys
from collections import deque
input = sys.stdin.readline

a = int(input().rstrip())
stack = deque([])

for i in range(a):
    n = input().rstrip()
    if n[0] == '1':
        stack.appendleft(n[2::])
    elif n[0]=='2':
        stack.append(n[2::])
    elif n=='3':
        if stack:
            print(stack[0])
            stack.popleft()
        else:
            print(-1)
    elif n=='4':
        if stack:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
    elif n=='5':
        print(len(stack))
    elif n=='6':
        if stack:
            print(0)
        else:
            print(1)
    elif n=='7':
        if stack:
            print(stack[0])
        else:
            print(-1)
    elif n=='8':
        if stack:
            print(stack[-1])
        else:
            print(-1)