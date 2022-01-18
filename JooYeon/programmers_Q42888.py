def solution(record):
    answer = []
    id_name = {}
    temp = []
    
    for r in record:
        uid = r.split()[1]
        if 'Enter' in r:
            name = r.split()[2]
            id_name[uid] = name
            temp.append(f"{uid}+님이 들어왔습니다.")
        elif 'Leave' in r:
            temp.append(f"{uid}+님이 나갔습니다.")
        elif 'Change' in r:
            name = r.split()[2]
            id_name[uid] = name

    for t in temp:
        answer.append(id_name[t.split('+')[0]]+t.split('+')[1])

    return answer
