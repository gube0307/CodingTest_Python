def solution(sides):
    max_value = max(sides)
    max_index = sides.index(max_value)
    sides.pop(max_index)
    if max_value < sides[0] + sides[1]:
        return 1
    else:
        return 2
    