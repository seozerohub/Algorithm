while True:
    a = int(input())
    if a==-1:
        break
    nlist = []
    for i in range(1,a):
        if a%i==0:
            nlist.append(i)

    if sum(nlist) == a:
        print("%d =" %(a), end='')
        for j in range(len(nlist)-1):
            print(" %d +" %(nlist[j]), end='')
        print(" %d" %nlist[len(nlist)-1])
    else:
        print("%d is NOT perfect." %(a))