def solution(emergency):
    answer = emergency.copy()
    answer.sort(reverse=True)
    answer2 = []
    for i in emergency:
        for j in answer:
            if i == j:
                answer2.append(answer.index(j)+1)                
    
    return answer2