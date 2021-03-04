# code 1
# def solution(participant, completion):
#     participant.sort() 
#     completion.sort() 
#     for i in range(len(completion)): 
#         if participant[i] != completion[i]: 
#             return participant[i] 
#     return participant[i+1]

##########################################################


# code 2
# import  collections
# def solution(participant, completion):
    
#     p = collections.Counter(participant)
#     c = collections.Counter(completion)
    
#     for i in p :
#         if i not in c.keys():
#             return i
        
#         if p.get(i) != c.get(i) :
#             return i

##########################################################


# code 3 
# 
# import collections

# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]
# 카운터 객체는 값을 뺄 수 있다 -> line 35