def solution(tickets):
    answer = []
    start_dest = {}
    
    tickets.sort(key=lambda x:x[1], reverse=True)
    
    # {출발지: [도착지 리스트]} 만들기
    for ticket in tickets:
        start = ticket[0]
        dest = ticket[1]
        if start not in start_dest:
            start_dest[start] = []
        start_dest[start].append(dest)

    
    stack = ['ICN']
    while len(stack):
        cur = stack[-1]
        # 공항 항공권이 없거나, 티켓을 다 쓴 경우 
        if cur not in start_dest or len(start_dest[cur]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(start_dest[cur].pop())

    return answer[::-1]
