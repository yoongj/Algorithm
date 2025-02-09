def solution(dartResult):
    dartResult= dartResult + '9'
    
    answer = 0
    before_score= 0 # 이전 점수
    score= 0        # 현재 점수
    
    temp= ''
    for i in dartResult:
        if i.isdigit() and temp=='':
            print('before_score', before_score)
            print('score', score)
            print('answer', answer)
            answer+= before_score
            before_score= score
            score= 0        
            print('before_score', before_score)
            print('score', score)
            print('answer', answer)
            print('\n')
        
        if i=='S':
            score+= int(temp)
            temp= ''
        elif i=='D':
            score+= int(temp)**2
            temp= ''
        elif i=='T':
            score+= int(temp)**3
            temp= ''
        
        if i=='*':
            before_score*= 2
            score*= 2
        elif i=='#':
            score*= -1
        
        if i.isdigit():
            temp= temp+i
        print('i',i, 'temp',temp)
        
    


    answer+= before_score
    return answer