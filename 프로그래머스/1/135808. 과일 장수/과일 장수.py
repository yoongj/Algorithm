def solution(k, m, score):
    answer = 0
    
    # 상자개수
    box= len(score)//m
    
    # 큰 점수 부터 나열
    scores= sorted(score)
    
    # 상자로 나누기
    for _ in range(box):
        for _ in range(m):
            lowest_score=scores.pop()
        answer+= lowest_score*m
    
    return answer