a = int(input())
b = int(input())
c = int(input())

gak = a+b+c
gaklist = [a,b,c]
setgak = set(gaklist)

if gak != 180:
    print("Error")
else:
    if a==60 and b==60 and c==60:
        print('Equilateral')
    elif len(setgak )==2:
        print('Isosceles')
    elif len(setgak)==3:
        print('Scalene')