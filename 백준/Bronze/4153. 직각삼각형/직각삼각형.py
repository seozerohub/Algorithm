import sys
input = sys.stdin.readline
while True:
    a,b,c = map(int, input().split())
    if a==0 and b==0 and c==0:
        break
    nlist = [a,b,c]
    nlist.sort()
    if nlist[0]**2 + nlist[1]**2 == nlist[2]**2:
        print("right")
    else:
        print("wrong")