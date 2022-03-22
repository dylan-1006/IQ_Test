# score calculator for basic mode
def basic_score(user_ans):
    CORRECT_ANS = ['B', 'D', 'B', '197', 'RUNNER', '35']
    position = 0
    score = 0
    for answer in user_ans:
        if answer == CORRECT_ANS[position]:
            score += 1
            print(score)

        position += 1

    return score


# score calculator for complex mode
def complex_score(user_ans):
    CORRECT_ANS = ['B', 'D', 'B', '197', 'RUNNER', '35']
    position = 0
    score = 0
    for answer in user_ans:
        if answer == CORRECT_ANS[position]:
            score += 1
            print(score)

        position += 1

    return score

