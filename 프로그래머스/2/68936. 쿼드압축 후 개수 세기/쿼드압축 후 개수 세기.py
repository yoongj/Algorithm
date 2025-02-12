def solution(arr):
    counter = [0, 0]
    
    for i in arr:
        counter[0]+= i.count(0)
        counter[1]+= i.count(1)
    
    def quad(arr, counter):

        long= len(arr)
        
        if long == 2:
            return counter
        
        for i in range(0,long, long//2):
            for j in range(0,long, long//2):
                # 한 파트 (1/4)
                part= [a[j:j+long//2] for a in arr[i:i+long//2]]
                
                # 압축 여부
                total= 0
                for row in part:
                    total+= sum(row)
                
                if total == 0:
                    counter[0]-= (long//2)**2 -1
                elif total == (long//2)**2:
                    counter[1]-= (long//2)**2 -1
                else:
                    counter= quad(part, counter)
        return counter            
    
    answer= quad(arr, counter)
    if answer== [0,4]:
        answer= [0,1]
    elif answer== [4,0]:
        answer= [1,0]
        
    return answer