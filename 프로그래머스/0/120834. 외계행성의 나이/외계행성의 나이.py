def solution(age):
    answer = ''
    list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    for i in str(age):
        answer += list[int(i)]
    return answer