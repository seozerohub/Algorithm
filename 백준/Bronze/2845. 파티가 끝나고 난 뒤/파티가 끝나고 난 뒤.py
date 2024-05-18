import sys
input = sys.stdin.readline
a,b = map(int,input().split())
r = a*b
a1,b1,c1,d1,e1 = map(int, input().split())
print(a1-r, b1-r, c1-r, d1-r, e1-r)