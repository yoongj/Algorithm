def solution(triangle):
    answer = 0
    
    for row in range(len(triangle)-1,0,-1): # row= 4, 3, 2, 1
        for col in range(row):
            triangle[row-1][col] += max(triangle[row][col], triangle[row][col+1])
    
    answer= triangle[0][0]            
            
        
    return answer