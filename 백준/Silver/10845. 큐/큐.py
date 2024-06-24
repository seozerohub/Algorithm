from collections import deque
import sys
input = sys.stdin.readline

stack = deque([])
n = int(input())

for i in range(n):
    a = input().rstrip()
    if a=='back':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif a== 'front':
        if stack:
            print(stack[0])
        else:
            print(-1)
    elif a=='empty':
        if len(stack)== 0:
            print(1)
        else:
            print(0)
    elif a=='size':
        print(len(stack))
    elif a=='pop':
        if stack:
            print(stack[0])
            stack.popleft()
        else:
            print(-1)
    else:
        stack.append(a[5::])