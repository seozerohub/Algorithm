T = int(input())
for i in range(T):
    nlist = list(input())
    stack = []
    p = True
    for j in range(len(nlist)):
        if nlist[j]=='(':
            stack.append('(')
        if nlist[j]==')':
            if stack and stack[-1]=='(':
                stack.pop(-1)
            else:
                p = False

    if stack == [] and p == True:
        print('YES')
    else:
        print('NO')