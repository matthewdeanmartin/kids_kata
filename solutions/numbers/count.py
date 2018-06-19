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


for x in range(1,100):
    say(str(x))
