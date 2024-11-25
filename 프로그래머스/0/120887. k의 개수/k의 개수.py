def solution(i, j, k):
    answer = 0
    k = str(k)
    for i in range(i, j+1):
        for j in str(i):
            if j == k:
                answer+=1
    return answer