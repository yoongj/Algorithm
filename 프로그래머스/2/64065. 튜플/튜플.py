def solution(s):
    sets=eval('['+s[1:-1]+']')
    answer = []
    
    sets.sort(key= len)
    result= set()
    for i in sets:
        answer.append(list(i-result)[0])
        result= i
    return answer