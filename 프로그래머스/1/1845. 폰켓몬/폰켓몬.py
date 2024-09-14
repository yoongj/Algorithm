from collections import Counter
def solution(nums):
    answer = 0
    
    num= len(nums)/2
    uniq= len(Counter(nums))
    
    return min(uniq, num)