def solution(k, score):
    answer= []
    legend = [float('-inf') for _ in range(k)]
    
    # 회차
    for i in score:

        minimum= min(legend)
        if minimum<i:
            legend[legend.index(minimum)]= i
        if min(legend) == float('-inf'):
            temp= legend.copy()
            while(float('-inf') in temp):
                temp.remove(float('-inf'))
            min_comp= min(temp)
        else:
            min_comp= min(legend)
        answer.append(min_comp)
    return answer