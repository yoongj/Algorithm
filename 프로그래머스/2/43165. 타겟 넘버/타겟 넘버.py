def solution(numbers, target):
    answer= 0
    
    def cal(numbers, ind):
        nonlocal answer
        
        if ind == len(numbers):
            # 계산 시작
            if sum(numbers) == target:
                answer+= 1
                
        else:
            cal(numbers,ind+1)
            numbers[ind]*= -1
            cal(numbers, ind+1)

    cal(numbers, 0)

    return answer