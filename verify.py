import sys
import time


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / 10)


def ismcq(answer):
    verify = False
    if answer.upper() == 'A' or answer.upper() == 'B' or answer.upper() == 'C' or answer.upper() == 'D':
        verify = True

    else:
        verify = False

    return verify


def isword(answer):
    verify = False
    if answer.isalpha():
        verify = True

    else:
        verify = False

    return verify


def isnumber(answer):
    verify = False
    if answer.isalpha() is False:
        verify = True

    else:
        verify = False

    return verify


def errormsg(verify, answer):
    if verify is False and answer != '':
        slowprint('Incorrect input type, please try again. \n\n')
