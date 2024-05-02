cnt = 0
while True:
    a = list(input().upper()) #hoe
    cnt = 0
    for i in range(len(a)):
        if a[i]=='A' or a[i]== 'E' or a[i]== 'I' or a[i]== 'O' or a[i]== 'U':
            cnt = cnt+1
    if a[i]=='#':
        break
    print(cnt)