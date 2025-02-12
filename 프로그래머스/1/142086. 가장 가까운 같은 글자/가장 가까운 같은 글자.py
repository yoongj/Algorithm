def solution(s):
    answer = []
    word_dic={}
    # word_dic= {w:ind for ind,w in enumerate(s)}
    for ind, i in enumerate(s):
        if i not in word_dic:
            word_dic[i]= ind
            answer.append(-1)
        else:
            answer.append(ind-word_dic[i])
            word_dic[i]= ind
    return answer