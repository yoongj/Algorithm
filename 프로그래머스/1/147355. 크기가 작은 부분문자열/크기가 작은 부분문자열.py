def solution(t, p):
    answer = 0
    
    long= len(p)
    for i in range(0, len(t)-long+1):
        if int(t[i:i+long]) <= int(p):
            answer+= 1
        
    return answer