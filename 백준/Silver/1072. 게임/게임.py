import math
x,y = map(int, input().split())
z = (y * 100) // x
z = math.floor(z)
i = 0
if z>=99:
    print(-1)
else:
    low, high = 1, 1000000000
    while low<=high:
        mid = (low + high) // 2
        z1 = ((y + mid) * 100) // (x + mid)
        z1 = math.floor(z1)

        if z1 > z:
            i = mid
            high = mid-1
        else:
            low = mid+1
    print(i)