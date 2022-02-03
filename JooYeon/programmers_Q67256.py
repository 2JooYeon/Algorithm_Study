def solution(numbers, hand):
    answer = ''
    
    # 키패드 맵 만들기
    num = list(range(1, 10))
    num += ['*', 0 , '#']
    coord = []
    for i in range(4):
        for j in range(3):
            coord.append([i, j])
    pad = dict(zip(num, coord))
            
        
    def compute_dist(cur, target):
        start = pad[cur]
        dest = pad[target]
        return abs(start[0]-dest[0]) + abs(start[1]-dest[1])
    
    
    l_cur = '*'
    r_cur = '#'
    
    for n in numbers:
        # 1,4,7 --> L
        if n in [1,4,7]:
            answer += 'L'
            l_cur = n
        # 3,6,9 --> R
        elif n in [3,6,9]:
            answer += 'R'
            r_cur = n
        # 2,5,8,0
        else:
            # 왼손 오른손 거리 비교
            l_dist = compute_dist(l_cur, n)
            r_dist = compute_dist(r_cur, n)
            # 왼손이 가까우면 
            if l_dist<r_dist:
                answer += 'L'
                l_cur = n
            # 오른손이 가까우면
            elif l_dist>r_dist:
                answer += 'R'
                r_cur = n
            # 거리가 같으면 
            else:
                # 왼손잡이
                if hand == 'left':
                    answer += 'L'
                    l_cur = n
                # 오른손잡이 
                else:
                    answer +='R'
                    r_cur = n
    
    return answer
