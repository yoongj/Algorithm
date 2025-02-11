def solution(number, limit, power):
    answer = 1
    
    if number!=1:
        for i in range(2,number+1):
            count= 0
            root= i**0.5
            for j in range(1,int(root)+1):
                if i%j== 0:
                    count+= 2
            if round(root,1)==root:
                count-= 1

            if count>limit:
                count= power
            answer+= count
            
    return answer