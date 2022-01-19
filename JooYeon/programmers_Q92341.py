def solution(fees, records):
    answer = []
    basic_time, basic_money, unit_time, unit_money = fees
    user_in_time = {}
    user_time_term = {}
    time_term = 0
    
    # 주차비 계산하는 함수 
    def check_money(time):
        if time <= basic_time: 
            return basic_money
        else: 
            if (time-basic_time) % unit_time:
                money = basic_money + (((time-basic_time)//unit_time)+1) * unit_money
            else:
                money = basic_money + ((time-basic_time)//unit_time) * unit_money
            return money
    
    
    for record in records:
        time_term = 0
        data = record.split()
        # 입차할 때 
        if data[2] == 'IN':
            user_in_time[data[1]] = data[0]
            if data[1] not in user_time_term:
                user_time_term[data[1]] = 0
        # 출차할 때 
        else:
            time_term = 0
            in_time = user_in_time[data[1]].split(':')
            out_time = data[0].split(':')
            user_in_time.pop(data[1])
            # 출차한 시각의 분 단위가 입차한 시각의 분 단위보다 클 때 
            if int(out_time[1]) < int(in_time[1]):
                time_term += 60 - (int(in_time[1]) - int(out_time[1]))
                # 시간 단위차에서 1시간 더 빼기 
                time_term += (int(out_time[0]) - int(in_time[0]) - 1)*60
            # 출차한 시각의 분 단위가 입차한 시각의 분 단위보다 작을 때 
            else:
                time_term += (int(out_time[1]) - int(in_time[1]))
                time_term += (int(out_time[0]) - int(in_time[0]))*60
            user_time_term[data[1]] += time_term

            
    # 입차하고 출차를 안한 경우 
    for user, in_time_str in user_in_time.items():
        time_term = 0
        in_time = in_time_str.split(':')
        time_term += (59 - int(in_time[1]))
        time_term += (23 - int(in_time[0]))*60
        user_time_term[user] += time_term
        
    for user in sorted(user_time_term):
        answer.append(check_money(user_time_term[user]))
        
    return answer
