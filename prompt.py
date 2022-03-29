import verify
import time
import sys


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / 10)


def prompt_basic():
    user_ans = []
    slowprint('\nAnswer all 10 questions. \n')

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

    # Q4
    answer = 'abc'
    print('\n\nQuestion 4')
    while not verify.isnumber(answer.strip()):
        time.sleep(1)
        print("What continues the below sequence?")
        slowprint(
            "\n975 \n319\n753\n... \n")
        answer = input('Enter a number:')
        verify.errormsg(verify.isnumber(answer.strip()), answer)

    user_ans.append(answer.upper())

    # Q5
    answer = ''
    print('\n\nQuestion 5')
    while not verify.isword(answer.strip()):
        time.sleep(1)
        print("Make a six-letter word out of these four letters.")
        slowprint(
            "\nE R N U \n")
        answer = input('Enter the word:')
        verify.errormsg(verify.isword(answer.strip()), answer)

    user_ans.append(answer.upper())

    # Q6
    answer = 'abc'
    print('\n\nQuestion 6')
    while not verify.isnumber(answer.strip()):
        time.sleep(1)
        print("The combined age of Archibald and Bertie is 19.")
        print('The combined age of Archibald and Charlie is 37')
        print('The combined age of Bertie and Charlie is 52')
        print('How old is Charlie ?')
        answer = input('\nEnter a number:')
        verify.errormsg(verify.isnumber(answer.strip()), answer)

    user_ans.append(answer.upper())

    # Q7
    answer = ''
    print('\n\nQuestion 7')
    while not verify.isword(answer.strip()):
        time.sleep(1)
        print("Which is the odd one out ?")
        slowprint(
            "\nram, lion, pig, goat, bull\n")
        answer = input('Enter the word:')
        verify.errormsg(verify.isword(answer.strip()), answer)

    user_ans.append(answer.upper())

    # Q8
    answer = ''
    print('\n\nQuestion 8')
    while not verify.isword(answer.strip()):
        time.sleep(1)
        print("The five letters below can be arranged to form a five-letter English word. Find the word.")
        slowprint(
            "\nT C I N A\n")
        answer = input('Enter the word:')
        verify.errormsg(verify.isword(answer.strip()), answer)

    user_ans.append(answer.upper())

    # Q9
    answer = 'abc'
    print('\n\nQuestion 9')
    while not verify.isnumber(answer.strip()):
        time.sleep(1)
        print("How many minutes is it before 12 noon if 12 minutes ago it was three times as many minutes past 9 am ?")
        answer = input('Please input your answer in minutes :')
        verify.errormsg(verify.isnumber(answer.strip()), answer)

    user_ans.append(answer.upper())

    # Q10
    answer = 'abc'
    print('\n\nQuestion 10')
    while not verify.isnumber(answer.strip()):
        time.sleep(1)
        print("What number should replace the question mark?")
        slowprint(
            "\n4328\n8567\n3124\n54?9\n")
        answer = input('Enter a number:')
        verify.errormsg(verify.isnumber(answer.strip()), answer)

    user_ans.append(answer.upper())

    # Transfer collected data back to main()
    return user_ans


def prompt_complex():
    user_ans = []
    slowprint('\nAnswer all 20 questions. \n')

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

    # Q4
    answer = 'abc'
    print('\n\nQuestion 4')
    while not verify.isnumber(answer.strip()):
        time.sleep(1)
        print("What continues the below sequence?")
        slowprint(
            "\n975 \n319\n753\n... \n")
        answer = input('Enter a number:')
        verify.errormsg(verify.isnumber(answer.strip()), answer)

    user_ans.append(answer.upper())

    # Q5
    answer = ''
    print('\n\nQuestion 5')
    while not verify.isword(answer.strip()):
        time.sleep(1)
        print("Make a six-letter word out of these four letters.")
        slowprint(
            "\nE R N U \n")
        answer = input('Enter the word:')
        verify.errormsg(verify.isword(answer.strip()), answer)

    user_ans.append(answer.upper())

    # Q6
    answer = 'abc'
    print('\n\nQuestion 6')
    while not verify.isnumber(answer.strip()):
        time.sleep(1)
        print("The combined age of Archibald and Bertie is 19.")
        print('The combined age of Archibald and Charlie is 37')
        print('The combined age of Bertie and Charlie is 52')
        print('How old is Charlie ?')
        answer = input('\nEnter a number:')
        verify.errormsg(verify.isnumber(answer.strip()), answer)

    user_ans.append(answer.upper())

    # Q7
    answer = ''
    print('\n\nQuestion 7')
    while not verify.isword(answer.strip()):
        time.sleep(1)
        print("Which is the odd one out ?")
        slowprint(
            "\nram, lion, pig, goat, bull\n")
        answer = input('Enter the word:')
        verify.errormsg(verify.isword(answer.strip()), answer)

    user_ans.append(answer.upper())

    # Q8
    answer = ''
    print('\n\nQuestion 8')
    while not verify.isword(answer.strip()):
        time.sleep(1)
        print("The five letters below can be arranged to form a five-letter English word. Find the word.")
        slowprint(
            "\nT C I N A\n")
        answer = input('Enter the word:')
        verify.errormsg(verify.isword(answer.strip()), answer)

    user_ans.append(answer.upper())

    # Q9
    answer = 'abc'
    print('\n\nQuestion 9')
    while not verify.isnumber(answer.strip()):
        time.sleep(1)
        print("How many minutes is it before 12 noon if 12 minutes ago it was three times as many minutes past 9 am ?")
        answer = input('Please input your answer in minutes :')
        verify.errormsg(verify.isnumber(answer.strip()), answer)

    user_ans.append(answer.upper())

    # Q10
    answer = 'abc'
    print('\n\nQuestion 10')
    while not verify.isnumber(answer.strip()):
        time.sleep(1)
        print("What number should replace the question mark?")
        slowprint(
            "\n4328\n8567\n3124\n54?9\n")
        answer = input('Enter a number:')
        verify.errormsg(verify.isnumber(answer.strip()), answer)

    user_ans.append(answer.upper())

    # Q11
    answer = ''
    print('\n\nQuestion 11')
    while not verify.ismcq(answer.strip()):
        time.sleep(1)
        print("What is the fear of fog?")
        slowprint(
            "\nA. homichlophobia \nB. acrophobia \nC. nosophobia  \nD. sitophobia \n")
        answer = input('Enter A,B,C or D:')
        verify.errormsg(verify.ismcq(answer.strip()), answer)

    user_ans.append(answer.upper())

    # Q12
    answer = ''
    print('\n\nQuestion 12')
    while not verify.isword(answer.strip()):
        time.sleep(1)
        print("What single word is concealed in this anagram?")
        slowprint(
            "\nITS IN CHARITY\n")
        answer = input('Enter the word:')
        verify.errormsg(verify.isword(answer.strip()), answer)

    user_ans.append(answer.upper())

    # Q13
    answer = 'abc'
    print('\n\nQuestion 13')
    while not verify.isnumber(answer.strip()):
        time.sleep(1)
        print("What number continues the sequence?")
        slowprint(
            "\n1\n10\n2.25\n8.25\n3.5\n6.5\n4.75\n")
        answer = input('Enter a number:')
        verify.errormsg(verify.isnumber(answer.strip()), answer)

    user_ans.append(answer.upper())

    # Q14
    answer = 'abc'
    print('\n\nQuestion 14')
    while not verify.isnumber(answer.strip()):
        time.sleep(1)
        print("At the zoo, the numbers of the animals’ cages were as  follows:")
        slowprint(
            "\nelephant 19\nseal 10\nmonkey 14\ncamel ?\n")
        print("What is the camel’s cage number?")
        answer = input('Enter a number:')
        verify.errormsg(verify.isnumber(answer.strip()), answer)

    user_ans.append(answer.upper())

    # Q15
    answer = 'abc'
    print('\n\nQuestion 15')
    while not verify.isnumber(answer.strip()):
        time.sleep(1)
        print("How many different arrangements of the word PUZZLES can you make?")
        answer = input('Enter a number:')
        verify.errormsg(verify.isnumber(answer.strip()), answer)

    user_ans.append(answer.upper())

    # Q16
    answer = 'abc'
    print('\n\nQuestion 16')
    while not verify.isnumber(answer.strip()):
        time.sleep(1)
        print("2 * 7 * 16 – (8 – 7) – (9 / 3) = x")
        print('Simplify and find the value of x')
        answer = input('Enter a number:')
        verify.errormsg(verify.isnumber(answer.strip()), answer)

    user_ans.append(answer.upper())

    # Q17
    answer = 'abc'
    print('\n\nQuestion 17')
    while not verify.isnumber(answer.strip()):
        time.sleep(1)
        print("What number should replace the question mark ?")
        slowprint(
            "\n4936:67\n2581:95\n1664:?\n")
        answer = input('Enter a number:')
        verify.errormsg(verify.isnumber(answer.strip()), answer)

    user_ans.append(answer.upper())

    # Q18
    answer = 'abc'
    print('\n\nQuestion 18')
    while not verify.isnumber(answer.strip()):
        time.sleep(1)
        print("If 48 = 60, what does 27 = ?")
        answer = input('Enter a number:')
        verify.errormsg(verify.isnumber(answer.strip()), answer)

    user_ans.append(answer.upper())

    # Q19
    answer = ''
    print('\n\nQuestion 19')
    while not verify.isword(answer.strip()):
        time.sleep(1)
        print("The five letters below can be arranged to form a five-letter English word. Find the word.")
        slowprint(
            "\nBURAM\n")
        answer = input('Enter the word:')
        verify.errormsg(verify.isword(answer.strip()), answer)

    user_ans.append(answer.upper())

    # Q20
    answer = ''
    print('\n\nQuestion 20')
    while not verify.isword(answer.strip()):
        time.sleep(1)
        print("Which is the odd one out?")
        slowprint(
            "\norange\npurple\nyellow\nblue\nlemon\n")
        answer = input('Enter the word:')
        verify.errormsg(verify.isword(answer.strip()), answer)

    user_ans.append(answer.upper())

    # Transfer collected data back to main()
    return user_ans
