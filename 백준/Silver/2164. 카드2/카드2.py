import sys
from collections import deque
input = sys.stdin.readline

stack = deque([])
a = input().rstrip()
a = int(a)

for i in range(1,a+1):
    stack.append(i)
for i in range(a-1):
    stack.popleft()
    stack.append(stack[0])
    stack.popleft()

print(*stack)