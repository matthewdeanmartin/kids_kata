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
    words = ["cat", "fart", "dog", "mom", "sister"]
    for word in words:
        say(word)
        say("What id I just say?")
        answer = input()

        if answer == word:
            say("good!")
        else:
            say("wrong! I did not say " + answer)


if __name__ == "__main__":
    run()