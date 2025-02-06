# 저주의 숫자 리스트에서 n번째 숫자는?
def solution(n):
    answer = 0
    
    num= list(range(1,200))
    num= [i for i in num if i%3 != 0]
    num= [i for i in num if '3' not in str(i)]
    
    print(len(num))
    answer= num[n-1]
    return answer