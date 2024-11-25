def solution(num_list, n):
    answer2 = []
    row = len(num_list) // n
    
    for i in range(row):
        answer = []
        for j in range(n):
            answer.append(num_list[i * n + j])
        answer2.append(answer)
    
    return answer2