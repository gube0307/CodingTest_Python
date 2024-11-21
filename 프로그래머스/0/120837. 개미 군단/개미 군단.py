def solution(hp):
    answer = 0
    a = 5
    b = 3
    c = 1
    answer += hp // a
    hp %= a
    answer += hp // b
    hp %= b
    answer += hp // c
    hp %= c
    return answer