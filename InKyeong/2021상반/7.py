from collections import deque

def solution(bridge_length, max_weight, wait_list):
    answer = 0
    on_list = deque([0] * bridge_length)
    on_weight = 0
    wait_list = deque(wait_list)
    while wait_list :
        answer += 1
        
        on_weight -= on_list.popleft()
        if(on_weight + wait_list[0]) <= max_weight :
            pop = wait_list.popleft()
            on_weight += pop
            on_list.append(pop)
        else :
            on_list.append(0)
        
            
    return answer + bridge_length