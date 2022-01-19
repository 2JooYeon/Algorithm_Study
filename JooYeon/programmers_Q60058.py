def solution(p):
    answer = ''
            
    def split_uv(p):
        lparen = 0
        rparen = 0
        
        for i in range(len(p)):
            if p[i]=='(': 
                lparen+=1
            else:
                rparen+=1
            if lparen == rparen:
                return p[:i+1], p[i+1:]
            
            
    def check_right_string(p):
        stack = []
        
        for word in p:
            if word == '(':
                stack.append(word)
            else:
                if not len(stack): return False
                stack.pop()
                
        if len(stack): return False
        else: return True
        
            
    def change_right_string(p):
        if not len(p):
            return ''
        else:
            u, v = split_uv(p)
            if check_right_string(u):
                return u + change_right_string(v)
            else:
                temp = '(' + change_right_string(v) + ')'
                new_u = ''
                for word in u[1:-1]:
                    if word == '(':
                        new_u += ')'
                    else:
                        new_u += '('
                return temp + new_u
            
    answer = change_right_string(p)
        
    return answer
