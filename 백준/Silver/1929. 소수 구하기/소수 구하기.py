
import sys
import math
input = sys.stdin.readline

a,b = map(int,input().split()) 

nlist = []

for i in range(b+1): 
    nlist.append(True)

for i in range(2,int(math.sqrt(b))+1):
    if nlist[i] == True:
        j = 2
        while i*j <= b: 
            nlist[i*j] = False
            j += 1

for i in range(2,b+1):
    if nlist[i]==True and a <= i:
        print(i)