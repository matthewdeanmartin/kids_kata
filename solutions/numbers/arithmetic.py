# coding=utf-8
"""
Write a counter that prints the numbers from 1 to 100
"""

def count():
    """
    1 2 3 4 5 ...
    
    :return: 
    """
    i = 0
    while True:
        i += 1
        print(i)
        if i > 100:
            break
    print("boom!"
          "")

count()
