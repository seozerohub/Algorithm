a,b,c = map(int, input().split())
nlist = [a,b,c]
if a+b+c >=100:
    print("OK")
else:
    if min(nlist) == a:
        print("Soongsil")
    elif min(nlist) == b:
        print("Korea")
    elif min(nlist) == c:
        print("Hanyang")