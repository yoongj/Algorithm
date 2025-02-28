from collections import deque

def solution(n, wires):
    
    que= deque()
    less_sub= float('inf')
    
    # 하나씩 제거하기
    for i in wires: # [1,3]이 없을 때
        visited= [ False for i in range(n+1)]
        wire= wires.copy()
        wire.remove(i)
        
        que.append(wire[0])
        ind=0
        while que:
            now= que.popleft()
            visited[now[0]]= True
            visited[now[1]]= True
            
            # if ind+1 == len(wire):
            #     continue
            wire.remove(now)
            for k in wire:         # 무엇이 나랑 붙어있는가
                if (now[0] in k) or (now[1] in k):
                    if k not in que:
                        que.append(k)
            ind += 1
        true= visited.count(True)
        false= n - true
        sub= abs(true-false)
        if sub<less_sub:
            less_sub= sub
    return less_sub