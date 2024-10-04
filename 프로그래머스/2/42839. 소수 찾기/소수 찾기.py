"""
"1782"의 경우
1   17  178 1782
        172 1728
    18  187 1872
        182 1827
    12  127 1278
        128 1287
        .
        .
        .
"""

def solution(numbers):
    answer= []
    cards= list(numbers)
    leng= len(cards)
    
    def make(making):
        # 0, 1 및 2가 아닌 짝수 제외 = 1보다 크고, 2를 제외한 홀수
        if int(making)>1 and (int(making)==2 or int(making)%2==1):
            answer.append(int(making))
        
        making= list(making)
        if len(making) == leng:
            return 
        
        # 나머지
        remainder= cards.copy()
        
        for i in making:
            remainder.remove(i)
        for i in remainder:
            new= ''.join(making)+i    
            
            make(new)
            
    for first in cards:
        make(first)
    
    # print(answer)
    # 중복제거
    answer= set(answer)
    # print(answer)
    
    # 소수 찾기
    prime_num=answer.copy()
    for i in answer:
        for j in range(3,i):
            if i%j == 0:
                prime_num.remove(i)
                break
    
    # print(prime_num)
    return len(prime_num)