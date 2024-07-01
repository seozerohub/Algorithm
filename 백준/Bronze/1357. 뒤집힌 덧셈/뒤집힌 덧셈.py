a,b = map(int,input().split())

def Rev(n):
    n = str(n)
    n = n[::-1]
    n = n.lstrip('0')
    return int(n)

print(Rev(Rev(a)+Rev(b)))