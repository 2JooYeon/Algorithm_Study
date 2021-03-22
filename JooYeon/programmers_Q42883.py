# def solution(number, k):
#     answer = ''
#     select = len(number) - k
#     index = 0
#
#     while 1:
#         target = max(number[index:len(number) - select + 1])
#         answer += target
#         index = number[index:len(number) - select + 1].find(target) + 1 + index
#         select -= 1
#         if index == len(number) - select:
#             answer += number[index:]
#             return answer
#         elif select == 0:
#             return answer

def solution(number, k):
    answer = ''
    data = [number[0]]
    for num in number[1:]:
        while len(data) > 0 and data[-1] < num and k > 0:
            k -= 1
            data.pop()
        data.append(num)
    if k > 0:
        data = data[:len(number)-k]
    answer = ''.join(data)
    return answer
