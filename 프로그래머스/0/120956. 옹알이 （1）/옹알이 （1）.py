def solution(babbling):
    answer = 0
    
    words= ['aya','ye', 'woo','ma']
    # combi= [w for w in words if]
    
    for i in babbling:
        for j in words:
            if j in i:
                i= i.replace(j,' ')
        if i.strip()=='':
            answer+=1
    
    return answer