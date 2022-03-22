import verify
import time
import sys
import calculation


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / 10)


def prompt_basic():
    user_ans = []

    # Q1
    answer = ''
    print('Question 1')
    while not verify.ismcq(answer.strip()):
        time.sleep(1)
        print("Which word is closest in meaning to the bold word below? \nESPOUSAL")
        time.sleep(2)
        slowprint("\nA. reverence\nB. adoption\nC. outbreak\nD. opinion \n")
        answer = input('Enter A,B,C or D:')
        verify.errormsg(verify.ismcq(answer.strip()), answer)

    user_ans.append(answer.upper())
    print(user_ans)

    # Q2
    answer = ''
    print('\n\nQuestion 2')
    while not verify.ismcq(answer.strip()):
        time.sleep(1)
        print("What is the meaning of sedition?")
        slowprint(
            "\nA. responsive to stimuli \nB. inducing calmness\nC. relating to drinks \nD. rebellious speech or action \n")
        answer = input('Enter A,B,C or D:')
        verify.errormsg(verify.ismcq(answer.strip()), answer)

    user_ans.append(answer.upper())
    print(user_ans)

    # Q3
    answer = ''
    print('\n\nQuestion 3')
    while not verify.ismcq(answer.strip()):
        time.sleep(1)
        print("Which is the odd one out?")
        slowprint(
            "\nA. bow \nB. portal\nC. rose \nD. bay \n")
        answer = input('Enter A,B,C or D:')
        verify.errormsg(verify.ismcq(answer.strip()), answer)

    user_ans.append(answer.upper())
    print(user_ans)

    # Q4
    print('\n\nQuestion 4')
    while not verify.isnumber(answer.strip()):
        time.sleep(1)
        print("What continues the below sequence?")
        slowprint(
            "\n975 \n319\n753\n... \n")
        answer = input('Enter a number:')
        verify.errormsg(verify.isnumber(answer.strip()), answer)

    user_ans.append(answer.upper())
    print(user_ans)

    # Q5
    print('\n\nQuestion 5')
    while not verify.isword(answer.strip()):
        time.sleep(1)
        print("Make a six-letter word out of these four letters.")
        slowprint(
            "\nE R N U \n")
        answer = input('Enter the word:')
        verify.errormsg(verify.isword(answer.strip()), answer)

    user_ans.append(answer.upper())
    print(user_ans)

    score = calculation.basic_score(user_ans)
    print(score)

    # Transfer collected data back to main()
    return user_ans


prompt_basic()
