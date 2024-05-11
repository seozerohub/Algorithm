while True:
    a, b, c = map(int, input().split())
    nlist = [a, b, c]
    nlist.sort()
    slist = set(nlist)
    if a==0 and b==0 and c==0:
        break
    else:
        if nlist[2] >= nlist[0] + nlist[1]:
            print("Invalid")
        else:
            if len(slist) == 1:
                print("Equilateral")
            elif len(slist) == 2:
                print("Isosceles")
            else:
                print("Scalene")