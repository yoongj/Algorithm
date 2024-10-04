# 1번 수포자: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

def solution(answers):
    count = [0, 0, 0]
    p1= [1,2,3,4,5]
    p2= [2, 1, 2, 3, 2, 4, 2, 5]
    p3= [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    len_Q= len(answers)
    result_1= [p1[(i%5)] for i in range(len_Q)]
    result_2= [p2[(i%8)] for i in range(len_Q)]
    result_3= [p3[(i%10)] for i in range(len_Q)]
    # print(result_1)
    # print(result_2)
    # print(result_3)
    
    for i in range(len_Q):
        if result_1[i]==answers[i]:
            count[0]+=1
        if result_2[i]==answers[i]:
            count[1]+=1
        if result_3[i]==answers[i]:
            count[2]+=1
    print(count)
    # print(count.max())
            
    answer= [i+1 for i,v in enumerate(count) if v==max(count)]
    
    return answer