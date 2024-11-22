def solution(n):
    answer2 = 0
    for i in range(1, n+1):
        answer = 0
        for j in range(1, i+1):
            if i % j == 0:
                answer += 1
        if answer >= 3:
            answer2 += 1
    return answer2