"""

Use pprint to print a dictionary of your attributes and skills, e.g. your name, age, grade, etc.

"""
import pprint

def print_resume():
    print("Max")

    resume = {
        "age" : 5,
        "typing speed" : 5,
        "run": True
    }
    pprint.pprint(resume)

print_resume()