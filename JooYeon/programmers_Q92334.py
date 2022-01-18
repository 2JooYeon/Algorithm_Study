def solution(id_list, report, k):
    answer = [0] * len(id_list)
    targetID_ids = {id: set() for id in id_list}
    
    report = set(report)
    
    for r in report:
        targetID_ids[r.split()[1]].add(r.split()[0])
    
    for id in id_list:
        if len(targetID_ids[id]) >= k:
            for who in targetID_ids[id]:
                answer[id_list.index(who)]+=1
        
        
    return answer
