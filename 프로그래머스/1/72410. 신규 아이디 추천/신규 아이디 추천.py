import re

def solution(new_id):
    answer = ''
    
    # 대문자 > 소문자
    # re.compile([A-Z]) 
    new_id= new_id.lower()
    
    # 소문자/숫자/-/_/. 만 사용가능
    for i in new_id:
        if i.isalnum() or (i in ['-','_','.']):
            answer= answer+i
    
    # 3단계
    while '..' in answer:
        answer= answer.replace('..','.')
        
    # 4단계
    answer= answer.strip('.')
    
    # 5단계
    if answer== '':
        answer= 'aaa'
    
    # 6단계
    elif len(answer) >= 16:
        answer= answer[:15]
        answer= answer.strip('.')
    
    # 7단게
    elif len(answer) <= 2:
        while len(answer) <=2:
            answer= answer+answer[-1]
    
    return answer