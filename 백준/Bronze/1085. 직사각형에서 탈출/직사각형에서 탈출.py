x,y,w,h = map(int, input().split())
list = [x,y,w,h,w-x,h-y]
print(min(list))