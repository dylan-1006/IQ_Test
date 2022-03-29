import prompt
import calculation
import results
import time
import sys

print('----------------------------------------------------------')
print('-                 Welcome to IQ Test                     -')
print('----------------------------------------------------------')
time.sleep(2)


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / 10)


def initialise():
    mode_verify = False

    while mode_verify is False:
        mode = input('\nPlease select the desired mode for this IQ Test [B (Basic) or C (Complex)]:')
        mode = mode.strip()
        if mode.upper() == 'B':
            mode_verify = True
            user_ans = prompt.prompt_basic()
            score = calculation.basic_score(user_ans)

        elif mode.upper() == 'C':
            mode_verify = True
            user_ans = prompt.prompt_complex()
            score = calculation.complex_score(user_ans)
        else:
            mode_verify = False
            print('Please enter [B] or [C] only')

    iq = results.score_to_iq(score)
    percentile = results.iq_percentile(iq)
    slowprint('\nCalculating your IQ......\n5% \n18% \n33% \n52% \n73%')
    time.sleep(1.5)
    slowprint('82%')
    time.sleep(1.5)
    slowprint('99% \n100% \nLoading......')
    time.sleep(2)
    slowprint('\nYour IQ is ' + str(iq) + ' and belongs to the ' + percentile + ' percentile. \n\n')
    retry()


def retry():
    retry_verify = False
    while retry_verify is False:
        startover = input('Do you wish to retry this IQ Test [Y or N] ? :')
        if startover.upper() == 'Y':
            retry_verify = True
            initialise()

        elif startover.upper() == 'N':
            retry_verify = True
            slowprint('Thanks for using this IQ test. Have a nice day!')

        else:
            retry_verify = False
            print('Please enter [Y] or [N] only.')


initialise()
