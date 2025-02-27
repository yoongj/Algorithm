def solution(dots):

    x= None
    y= None
    
    for i in dots:
        if x == None:
            x, y= i[0], i[1]
        else:
            if x!= i[0]:
                width= abs(x-i[0])
            if y!= i[1]:
                height= abs(y-i[1])
    return width*height