T = int(input())

for j in range(T):
    n = int(input())
    cnt = 0
    left = 1
    right = 10 ** 16
    while left <= right:
        mid = (left +right)//2
        ds = (mid*(mid+1))//2
        if ds < n:
            cnt = mid
            left = mid +1
        elif ds > n:
            right = mid -1
        else:
            cnt = mid
            break

    print(cnt)