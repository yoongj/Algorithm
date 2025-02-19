def solution(n):
    
    length= 0
    pyramid= []
    for i in range(1,n+1):
        pyramid.append([0 for _ in range(i)])
        length+= i
    
    arrow_list= ['down', 'right','up'] # (0)down > (1)right > (2)up 순
    arrow= 0
    row= 0
    col= 0
    for i in range(1, length+1):
        pyramid[row][col]= i
        if i == length:
            break

        if arrow_list[arrow] == 'down':
            if row==n-1 or pyramid[row+1][col] != 0:
                arrow+= 1
            else:
                row+= 1
        if arrow_list[arrow] == 'right':
            if col==row or pyramid[row][col+1] != 0:
                arrow+= 1
            else:
                col+= 1
        if arrow_list[arrow] == 'up':
            if row==0 or pyramid[row-1][col-1] != 0:
                arrow= 0
            else:    
                row-= 1
                col-= 1
                
            if arrow_list[arrow] == 'down':
                if row==n-1 or pyramid[row+1][col] != 0:
                    arrow+= 1
                else:
                    row+= 1
    
          
    return sum(pyramid,[])