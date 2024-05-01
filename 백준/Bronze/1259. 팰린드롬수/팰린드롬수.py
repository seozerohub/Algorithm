while True:
    a = str(input())
    if a == '0':
        break;
    else:
        a = list(a)
        b = a[::-1]
        if a==b:
            print('yes')
        else:
            print('no')