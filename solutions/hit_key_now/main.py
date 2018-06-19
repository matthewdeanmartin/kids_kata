"""

Write a game that waits for the user to hit enter, then waits for any key.

If it took between 4.75 or 5.25 seconds, then they win.

If it is more, print "too slow!"

If it is less, print "too fast!"

"""
import math
import time


def play_game():
    print("When ready, hit keyboard to start. Then hit any key exactly 5 seconds later")
    ready = input("Are you ready to play?")
    start = time.time()

    print("Hit a key in 5 seconds!")
    done = input("go")
    finish = time.time()
    duration = finish - start
    print(duration)
    off_by = math.fabs(duration - 5.0)
    if off_by < .25:
        print("Bang on!")
        return
    if duration < 5:
        print("Too fast!")
    if duration > 5:
        print("Too slow")


if __name__ == "__main__":
    play_game()
