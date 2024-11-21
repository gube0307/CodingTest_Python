def solution(slice, n):
    answer = 0
    while(n > 0):
        n = n - slice
        answer += 1
    return answer