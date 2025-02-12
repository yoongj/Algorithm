def solution(n, m):
    answer = []
    small= min(n,m)
    big= max(n,m)
    
    # 최대공약수 
    gcf= 0
    for i in range(1, small+1):
        if (small%i == 0) and (big%i == 0):
            if i > gcf:
                gcf= i
    answer.append(gcf)
    
    # 최소공배수
    k= 1
    while(1):
        if (big*k)%small == 0:
            answer.append(big*k)
            break
        else:
            k+= 1 
                
    return answer