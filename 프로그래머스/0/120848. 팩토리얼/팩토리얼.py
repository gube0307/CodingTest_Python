def solution(n):
    answer = 0
    answer2 = 1
    while(True):
        answer += 1
        answer2 *= answer
        if answer2 == n:
            return answer
        if answer2 > n:
            return answer-1