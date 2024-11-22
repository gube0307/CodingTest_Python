def solution(box, n):
    answer = 1
    a = 0
    for i in box:
        a = i//n
        answer *= a
    return answer
