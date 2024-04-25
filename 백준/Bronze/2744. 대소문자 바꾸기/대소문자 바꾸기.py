word = list(input())
wordlist = list()
for i in range(len(word)):
    word[i] = ord(word[i])
    if word[i] > 90:
        word[i] = chr(word[i])
        w = word[i].upper()
        wordlist.append(w)
    else:
        word[i] = chr(word[i])
        w = word[i].lower()
        wordlist.append(w)

for j in wordlist:
    print(j, end='')