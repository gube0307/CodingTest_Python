def solution(num, k):
    answer = 0
    num = str(num)
    for i in num:
        if int(i) == k:
            answer = num.index(i)+1
            break
        else:
            answer = -1
    return answer