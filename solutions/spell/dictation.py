"""
Ask the user to dictate a sentance. Say a word, wait for user to type it, say next word. etc.
"""
from subprocess import call


def say(word):
    """

    :type word: str
    :return:
    """
    print(word, end=" ")
    call(["say", word])

def say_quiet(word):
    """

    :type word: str
    :return:
    """
    call(["say", word])

def run():
    sentence = "Beings are countless. I vow to liberate them all"
    say(sentence)
    words = sentence.split()
    for word in words:
        say(word)
        wrong = True
        while wrong:
            answer = input()

            if answer == word:
                wrong =False
            else:
                say_quiet("nope! " + word)


if __name__ == "__main__":
    run()