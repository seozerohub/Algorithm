Nlist = []
N = int(input())
a = N//5
for i in range(a+1): #4
    B = 5*i
    A = (1/3)*(N-B)
    if A%1==0:
        A = int(A)
        r = A+i
        Nlist.append(r)

if Nlist == []:
    print(-1)
else:
    print(int(min(Nlist)))