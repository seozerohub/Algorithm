def solution(array):
    d = dict() # d = {1:2, 2:2}
    for i in array:
        if i in d:
            d[i] = d[i]+1
        else:
            d[i]=1
    
    
    max_v = max(d.values()) # 값 2
    m = []
    for k,v in d.items(): # [(1,2), (2,2)]
        if max_v == v:
            m.append(k)
    
    if len(m) == 1:
        result = max(d, key = d.get)
    else:
        result = -1
    
    
    return result