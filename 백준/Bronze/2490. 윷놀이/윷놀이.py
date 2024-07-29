alist = list(map(int, input().split()))
blist = list(map(int, input().split()))
clist = list(map(int, input().split()))

def F(x):
    cnt = 0
    for i in x:
        if i == 0:
            cnt+=1

    if cnt == 0:
        return print("E")
    elif cnt == 1:
        return print("A")
    elif cnt == 2:
        return print("B")
    elif cnt == 3:
        return print("C")
    elif cnt == 4:
        return print("D")

F(alist)
F(blist)
F(clist)