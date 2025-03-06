def solution(n, words):
    # answer = []
    
    conducted= []
    person= 1
    # count= 1
    
    for ind, w in enumerate(words):
        print('person',person, 'word', w)
                
        count= (ind // n)+1
        print(count)
        
        if w in conducted :
            print('걸렸다')
            break
        if conducted and w[0]!=conducted[-1][-1] :
            print('틀렸다')
            break
        
        conducted.append(w)
        person+= 1        
        if person>n:
            person= 1
        
    if len(conducted)==len(words):
        person= 0
        count= 0
        
    return [person, count]