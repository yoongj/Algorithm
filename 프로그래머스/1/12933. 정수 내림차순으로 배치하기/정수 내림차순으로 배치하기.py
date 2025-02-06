def solution(n):
    answer = 0
    
    an= sorted(str(n), reverse= True)
    return int(''.join(an))