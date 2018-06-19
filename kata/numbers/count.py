"""
Using the provided function, make the computer read the numbers aloud from 1-10 or more!
"""

from subprocess import call

def say(word):
    """

    :type word: str
    :return:
    """
    print(word)
    call(["say", word])


def go():
    # code goes here.
    pass


go()