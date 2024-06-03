import sys
input = sys.stdin.readline

a = int(input().rstrip())
stack = []
for i in range(a):
    n = input().rstrip()
    n = int(n)
    if n==0:
        stack.pop(-1)
    else:
        stack.append(n)

print(sum(stack))