a = int(input())
slist = ['Never gonna give you up', 'Never gonna let you down', 'Never gonna run around and desert you', 'Never gonna make you cry', 'Never gonna say goodbye', 'Never gonna tell a lie and hurt you', 'Never gonna stop']
cnt = 0
for i in range(a):
    s = input()
    for j in slist:
        if s==j:
            cnt+=1
if cnt==a:
    print("No")
else:
    print("Yes")