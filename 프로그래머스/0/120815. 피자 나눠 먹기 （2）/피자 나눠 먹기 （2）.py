def solution(n):
    answer = 1
    pizza = 0
    while(True):
        pizza += 6
        if pizza % n == 0:
            return answer
            break
        answer +=1
    return answer