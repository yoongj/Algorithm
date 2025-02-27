def solution(numbers, k):
    answer = 0
    
    count= 2*k -1
    
    answer= count%len(numbers)
    if answer == 0:
        answer= numbers[-1]
    return answer