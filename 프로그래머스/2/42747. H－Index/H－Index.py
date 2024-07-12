def solution(citations):
    
    for h in range(len(citations),-1,-1):    # 5,4,3,2,1 ... 0도 포함!
        answer = 0
        for i in citations:
            if i >= h:
                answer += 1
        if h <= answer:
            break
    
    return h