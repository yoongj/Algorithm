from collections import Counter
def solution(participant, completion):
    # 두 리스트를 카운트한 뒤 차집합을 구함
    participant_count = Counter(participant)
    completion_count = Counter(completion)
    
    # completion에 없는 사람, 즉 차집합 구하기
    answer = participant_count - completion_count
    
    # answer는 딕셔너리 형태로 남은 사람이므로, key만 추출해서 반환
    return list(answer.keys())[0]