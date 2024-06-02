import sys
input = sys.stdin.readline
a = int(input().rstrip())
stack = []
for i in range(a):
    s = input().rstrip()
    s = s.replace(" ", "")
    if s=='top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif s== 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif s == 'size':
        print(len(stack))
    elif s == 'pop':
        if stack:
            print(stack[-1])
            stack.pop(-1)
        else:
            print(-1)
    else:
        stack.append(s[4::])
