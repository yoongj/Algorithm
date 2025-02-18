def solution(n):
    answer= [[]]
    
    def hanoi(n, start, end, mid):
        if n== 1:
            return [[start, end]]
        else: # (1>2) + [1,3] + (2>3)
            return hanoi(n-1, start,mid,end) + [[start,end]] + hanoi(n-1, mid,end,start)

    
    return hanoi(n, 1,3,2)