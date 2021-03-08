def solution(bridge_length, weight, truck_weights):
    answer = bridge_length
    bridge_list = []
    index = 0
    while (index <= len(truck_weights) - 1):
        if len(bridge_list) < bridge_length:
            if sum(bridge_list) + truck_weights[index] <= weight:
                bridge_list.append(truck_weights[index])
                index += 1
                if index == len(truck_weights):
                    answer += len(bridge_list)
                    break
            else:
                bridge_list.append(0)

        elif len(bridge_list) == bridge_length:
            del bridge_list[0]
            answer += 1

    return answer