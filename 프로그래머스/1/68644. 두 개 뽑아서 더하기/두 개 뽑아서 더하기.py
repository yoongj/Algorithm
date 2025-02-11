def solution(numbers):
    answer = []
    
    long= len(numbers)
    for index, i in enumerate(numbers):
        for j in range(index+1, long):
            plus= i+numbers[j]
            if plus not in answer:
                answer.append(plus)
    answer.sort()
    return answer