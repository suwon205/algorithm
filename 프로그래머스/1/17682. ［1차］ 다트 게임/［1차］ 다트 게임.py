def solution(dartResult):
    answer = 0
    score = ''
    record = []
    for dart in dartResult:
        if dart.isdigit():
            score += dart
        elif dart == "D":
            record.append(int(score) ** 2)
            score = ""
        elif dart == "T":
            record.append(int(score) ** 3)
            score = ""
        elif dart == "S":
            record.append(int(score))
            score = ""
        elif dart == "#":
            record[-1] *= -1
        elif dart == "*":
            record[-1] *= 2
            if len(record) >= 2:
                record[-2] *= 2

    answer = sum(record)
    print(record)
    return answer