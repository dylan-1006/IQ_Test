import random
import time


print('----------------------------------------------------------')
print('-                 Welcome to IQ test                     -')
print('----------------------------------------------------------')
time.sleep(2)

score = 0

''' Questions 1 '''
def answer1():
    global score
    score = 0
    ans = str(input('Please input your answer :'))
    if ans == 'Ban':
        score = score + 1
    elif ans == 'Bane' or 'Bun' or 'Band' :
        score = score + 0
    else:
        print('Please enter a valid answer')
        answer1()
    
def question1():
    print('')
    print('Question 1:')
    print('Insert the word that completes the first word and begins the second. Ur (...) AI')
    time.sleep(4)
    list = ['Band', 'Bun', 'Bane', 'Ban']
    random.shuffle(list)
    for x in range(len(list)):
        print(list[x])
    time.sleep(4)
    answer1()
 
question1()
print(score)
