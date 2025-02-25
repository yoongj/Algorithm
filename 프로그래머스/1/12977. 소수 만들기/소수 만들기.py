def solution(nums):
    answer = 0
    length= len(nums)

    for ind_a, a in enumerate(nums):
        ind_b= ind_a+1
        if ind_a +2 == length:
            break
        for b in nums[ind_b:]:
            if ind_b +1 == length:
                break
            for c in nums[ind_b+1:]:
                target= a+b+c
                signal= 0
                for t in range(2, target):
                    if target%t == 0:
                        signal+= 1
                        break
                    
                if signal != 1:
                    answer += 1
            ind_b += 1

    return answer