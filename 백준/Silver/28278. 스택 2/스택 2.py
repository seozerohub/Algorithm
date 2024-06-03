import sys
input = sys.stdin.readline
a = int(input().rstrip())
stack = []

for i in range(a):
    n = input().rstrip()
    if n[0]=='1':
        stack.append(n[2::])
    elif n[0]=='2':
        if stack:
            print(stack[-1])
            stack.pop(-1)
        else:
            print(-1)
    elif n[0]=='3':
        print(len(stack))
    elif n[0]=='4':
        if stack:
            print(0)
        else:
            print(1)
    elif n[0]=='5':
        if stack:
            print(stack[-1])
        else:
            print(-1)
