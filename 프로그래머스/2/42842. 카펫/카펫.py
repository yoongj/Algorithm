def solution(brown, yellow):
    answer = []
    
    square= []
    for i in range(1,yellow+1):
        if yellow%i == 0:
            square.append([yellow//i,i])
    
    print('square',square)
    for i in square:
        if (i[0]+2) * (i[1]+2) == brown+yellow:
            print('i',i)
            answer= [i[0]+2,i[1]+2]
            break
    
    return answer