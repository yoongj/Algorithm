def solution(n, arr1, arr2):
    answer = []
    
    map1= [[' ']*n for _ in range(n)]
    map2= [[' ']*n for _ in range(n)]
    
    for num, i in enumerate(arr1):
        for j in range (n-1,-1,-1):
            if i - 2**j >=0:
                i-= 2**j
                map1[num][n-1-j]= '#'
                
    for num, i in enumerate(arr2):
        for j in range (n-1,-1,-1):
            if i - 2**j >=0:
                i-= 2**j
                map2[num][n-1-j]= '#'
    
    for num_i, i in enumerate(map1):
        for num_j, j in enumerate(i):
            if j == '#':
                map2[num_i][num_j]= '#'
    
    for i in map2:
        answer.append(''.join(i))
        
                
    return answer