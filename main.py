import random
import time

print('----------------------------------------------------------')
print('-                 Welcome to IQ test                     -')
print('----------------------------------------------------------')
time.sleep(2)

score = 0

'''   Questions  '''


def question1():
    print('')
    print('Question 1:')
    time.sleep(2)
    print('473982 is to 1419')
    time.sleep(2)
    print('329684 is to 1418')
    time.sleep(2)
    print('therefore')
    print('751694 is to (...) ?')
    time.sleep(2)
    global score
    ans = str(input('Please input your answer :'))
    if ans.isdigit():
        ans = int(ans)
        if ans == 1319:
            score = score + 1
        else:
            score = score + 0
    else:
        print('Please enter a digit')


def question2():
    print('')
    print('Question 2:')
    time.sleep(2)
    print('Which word in brackets is closest in meaning to the word in capitals?')
    time.sleep(5)
    print('ESPOUSAL')
    time.sleep(2)
    print('(reverence, adoption, outbreak, opinion, invitation)?')
    time.sleep(2)
    global score
    ans = str(input('Please input your answer :'))
    if ans.isalpha():
        ans = ans.upper()
        if ans == 'ADOPTION':
            score = score + 1
        else:
            score = score + 0
    else:
        print('Please enter a word from the bracket.')


def question3():
    print('')
    print('Question 3:')
    time.sleep(2)
    print('Solve the anagram in brackets to complete the quotation')
    time.sleep(5)
    print('Writing about music is like dancing about')
    print('(ERECT HAIRCUT)')
    time.sleep(2)
    global score
    ans = str(input('Please input your answer :'))
    if ans.isalpha():
        ans = ans.upper()
        if ans == 'ARCHITECTURE':
            score = score + 1
        else:
            score = score + 0
    else:
        print('Please enter a word.')


def question4():
    print('')
    print('Question 4:')
    time.sleep(2)
    print('What is the meaning of sedition?')
    time.sleep(5)
    print('A : responsive to stimuli')
    time.sleep(2)
    print('B : inducing calmness')
    time.sleep(2)
    print('C : relating to drinks')
    time.sleep(2)
    print('D : rebellious speech or action')
    time.sleep(2)
    print('E : deposit of rock fragments')
    global score
    ans = str(input('Please input your answer [A,B,C,D]:'))
    if ans.isalpha():
        ans = ans.upper()
        if ans == 'D':
            score = score + 1
        else:
            score = score + 0
    else:
        print('Please enter a word from the bracket.')


def question5():
    print('')
    print('Question 5:')
    time.sleep(2)
    print('Which is the odd one out ?')
    time.sleep(3)
    print('bow, portal, rose, bay, lancet')
    time.sleep(2)
    global score
    ans = str(input('Please input your answer :'))
    if ans.isalpha():
        ans = ans.upper()
        if ans == 'PORTAL':
            score = score + 1
        else:
            score = score + 0
    else:
        print('Please enter a word.')


def question6():
    print('')
    print('Question 6:')
    time.sleep(2)
    print('975, 319, 753')
    time.sleep(3)
    print('What continues the above sequence ?')
    time.sleep(2)
    global score
    ans = str(input('Please input your answer :'))
    if ans.isdigit():
        ans = int(ans)
        if ans == '197':
            score = score + 1
        else:
            score = score + 0
    else:
        print('Please enter a word.')


''' retry function '''


def retry(a1, b1):
    startover = input('Do you want to retry this question [Y or N] ?')
    startover = startover.upper()
    if startover == 'Y':
        a1
    else:
        conti = input('Do you wish to continue to the next question or end the test? [next / end] :')
        conti = conti.upper()
        if conti == 'NEXT':
            b1
        else:
            print('Thanks for trying out IQ test')

