"""
Create a typing game where the computer says a word and the user must type it.

This will require iterating a list, using if-else blocks.
"""
from subprocess import call

def say(word):
    """

    :type word: str
    :return:
    """
    print(word)
    call(["say", word])

def run():
    pass


if __name__ == "__main__":
    run()