"""
Ask the user to dictate a sentance. Say a word, wait for user to type it, say next word. etc.
"""
from subprocess import call


def say(word):
    """
    Easier
    :type word: str
    :return:
    """
    print(word, end=" ")
    call(["say", word])

def say_quiet(word):
    """
    Harder
    :type word: str
    :return:
    """
    call(["say", word])

def run():
   pass


if __name__ == "__main__":
    run()