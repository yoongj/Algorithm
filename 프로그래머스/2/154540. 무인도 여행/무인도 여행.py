from collections import deque

def solution(maps):
    answer = []
    maps= [list(map(lambda x: int(x) if x.isdigit() else x, i)) for i in maps]
    # print('maps',maps)
    
    que= deque()
    visited= [[True if j=='X' else False for j in i] for i in maps]
    # print('visit',visited)
    
    for row in range(len(maps)):
        for col in range(len(maps[0])):
            
            if not visited[row][col]:
                que.append((row,col))
                visited[row][col]= True
                days= 0
                while que:
                    # print(que)
                    r, c= que.popleft()
                    # visited[r][c]= True
                    days+= maps[r][c]
                    # print('days', days)
                    # 상
                    if r!= 0 and visited[r-1][c]==False:
                        que.append((r-1,c))
                        visited[r-1][c]= True
                        # print(f'({r},{c}) 위에 ({r-1},{c}) 있음')
                    # 하
                    if r!= len(maps)-1 and visited[r+1][c]==False:
                        que.append((r+1,c))
                        visited[r+1][c]= True
                        # print(f'({r},{c}) 아래에 ({r+1},{c}) 있음')
                    # 좌
                    if c!= 0 and visited[r][c-1]==False:
                        que.append((r,c-1))
                        visited[r][c-1]= True
                        # print(f'({r},{c}) 왼쪽에 ({r},{c-1}) 있음')
                    # 우
                    if c!= len(maps[0])-1 and visited[r][c+1]==False:
                        que.append((r,c+1))
                        visited[r][c+1]= True
                        # print(f'({r},{c}) 오른쪽에 ({r},{c+1}) 있음')
                
                answer.append(days)
                    
    if not answer:
        answer= [-1]
    
    answer.sort()
    return answer