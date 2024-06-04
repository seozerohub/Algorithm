'''
([)]
([append  )pass ]pop(-1)
'''

import sys
input = sys.stdin.readline

while True:
    stack =[]
    nlist = list(input().rstrip())
    if nlist[0]=='.':
        break
    p = True
    for i in nlist:
        if i=='(':
            stack.append('(')
        elif i=='[':
            stack.append('[')
        elif i==')':
            if stack and stack[-1]=='(':
                stack.pop(-1)
            else:
                p = False
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop(-1)
            else:
                p = False
                break
    if len(stack)== 0 and p:
        print('yes')
    else:
        print('no')