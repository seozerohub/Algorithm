def solution(s):
    temp =""
    result = ""
    numlist = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    for i in s: # one4seveneight
        if i.isnumeric():
            result = result + i
        else:
            temp = temp + i
            if temp in numlist:
                result = result+ str(numlist.index(temp))
                temp="" 
    answer = int(result)
    return answer