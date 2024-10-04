def solution(sizes):
    max_size= [0,0]
    
    for i in sizes:
        i.sort()
        w,h = i
        if max_size[0]<w:
            max_size[0]= w
        if max_size[1]<h:
            max_size[1]= h
        # print(max_size)
    
    return max_size[0]*max_size[1]