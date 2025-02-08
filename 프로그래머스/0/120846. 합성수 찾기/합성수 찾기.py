def solution(n):
    if n<4:
        answer= 0
    
    else:
        answer= n-3
        
        # 약수가 두 개 인 경우 (제외할 경우 카운팅)
        count= 0
        for i in range(1,n+1):
            print('\ni',i)
            if i>3 and i%2==1: # 5이상이고, 홀수 중에
                # 약수가 있는 수를 제외
                for j in range(3,i):
                    print('  j',j)
                    if i%j==0:
                        break
                    if j==i-1:
                        answer-=1
                        print('>> i',i, 'j',j)         
        
    return answer