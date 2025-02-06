from collections import deque

def solution(d, budget):
    answer = 0
    
    # depart= deque(sorted(d))
    
    # while budget > 0:
    #     price = depart.popleft()
    #     budget -= price
    #     if budget>= 0:
    #         answer+= 1
    
    
    for price in sorted(d):
        budget -= price
        if budget >= 0:
            answer+= 1

    return answer