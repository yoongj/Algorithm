def solution(keymap, targets):
    answer = []
    
    key_count= {}
    for i in keymap:
        for index, alpha in enumerate(i):
            if alpha not in key_count:
                key_count[alpha]= index+1
            else:
                key_count[alpha]= min(key_count[alpha], index+1)
    
    for i in targets:
        count= 0
        for j in i:
            try :
                count+= key_count[j]
            except:
                count= -1
                break
        answer.append(count)
    return answer