from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    def bfs(begin, target, words, visited):
        queue = deque([(begin, 0)])
        visited[0] = 1
        while queue:
            cur_word, count = queue.popleft()
            # cur_word가 target과 같을 경우 현재 카운트 값을 반환 
            if cur_word == target:
                return count
            # word가 target과 다를 경우
            for i in range(len(words)):
                diff = 0
                # 알파벳 차이가 1개인 단어 찾기 
                for c1, c2 in zip(cur_word, words[i]):
                    if c1 != c2:
                        diff += 1
                if diff == 1:
                    queue.append((words[i], count+1))
                    visited[i] = 1
    answer = 0
    visited = [0]*len(words)
    answer = bfs(begin, target, words, visited)
                
    return answer
