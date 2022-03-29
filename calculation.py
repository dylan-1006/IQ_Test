# score calculator for basic mode
def basic_score(user_ans):
    CORRECT_ANS = ['B', 'D', 'B', '197', 'RUNNER', '35', 'LION', 'ANTIC', '42', '5']

    position = 0
    score = 0
    for answer in user_ans:
        if answer == CORRECT_ANS[position]:
            score += 1

        position += 1

    score = score * 4

    return score


# score calculator for complex mode
def complex_score(user_ans):
    CORRECT_ANS = ['B', 'D', 'B', '197', 'RUNNER', '35', 'LION', 'ANTIC', '42', '5', 'A', 'CHRISTIANITY', '6', '12',
                   '2520', '110', '48', '33', 'UMBRA', 'LEMON']

    position = 0
    score = 0
    for answer in user_ans:
        if answer == CORRECT_ANS[position]:
            score += 1

        position += 1

    score = score * 2

    return score
