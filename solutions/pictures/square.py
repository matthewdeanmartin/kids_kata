# coding=utf-8
"""
Ways to print a square
"""
# This is one way to print a square. See if you can do it in fewer lines of code using loops.
# def string_literal_square():
#     print("""
#     ##########
#     #        #
#     #        #
#     #        #
#     #        #
#     ##########
#     """)

def loops_square():
    print(    "##########")
    for i in range(0,5):
        print("#        #")
    print("##########")




def top_bottom():
    print("##########")

def better_loops_square():
    top_bottom()
    for i in range(0,5):
        print("#        #")
        top_bottom()

def sized_top_bottom(size):
    for i in range(0, size):
        print("#", end="")
    print()

def resizable_square(size):
    top_bottom()
    for i in range(0, 5):
        print("#", end="")
        for j in range(0, size-2):
            print(" ", end="")
        print("#")
        top_bottom()
