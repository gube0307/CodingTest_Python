def solution(order):
    answer = 0
    order = str(order)
    for i in order:
        if int(i) == 0:
            continue
        if int(i) % 3 == 0:
            answer += 1
    return answer