"""
Shyne Choi, Lucas Lee, Edwin Zheng
SoftDev
k05 -- A Program to Print a SoftDev Student's Name But Amalgamated
2021-28-21
"""

# SUMMARY OF TRIO DISCUSSION
# Decided on combining the code, using both approaches based on number of arguments passed on the command line
# If two filenames are given, the program will use those files to create the period lists
# If none are given, the user is prompted to provide the names directly, using 'exit' to stop the input
# DISCOVERIES
# Needed to properly sanitize and handle exceptions in user input
# QUESTIONS
# Should the names be pulled randomly?
# And should period size be taken into account when choosing the random name?
# COMMENTS
# N/A

import sys
from random import randrange

def read_names(filename: str):
    """
    Reads a text file containing a list of names, where each line contains
    one name, and returns a list of the names.
    """

    file_contents = ""
    with open(filename, "r") as f:
        file_contents = f.read()
    names = file_contents.split("\n")

    # Remove empty lines
    names = [name for name in names if name]
    return names

def addToList():
    """
    Prompts the user in a loop for the period and name of the Student
    If 'exit' is given for the period, the loop stops and returns the names
    """

    pd1 = []
    pd2 = []

    while True:
        period = input("What period is the student in?\n")

        # Checks if the person wishes to stop typing
        if period.strip().lower() == 'exit':

            # Ensures there is a name to choose
            if len(pd1) + len(pd2) == 0:
                print("Please input at least one name")
                continue
            else:
                return (pd1, pd2)

        # Checks if the user inputed an actual number
        try:
            period = int(period)
        except:
            print("That is not a softdev period. Please input the information again.")
            continue

        name = input("What is their name?\n")

        # Checks if the period number is valid
        if period == 1:
            pd1.append(name)
        elif period == 2:
            pd2.append(name)
        else:
            print("That is not a softdev period. Please input the information again.")
            continue

        print("The student's name is " + name + " and their period is " + str(period) + ".")

def main():
    """
    Prints a random student name given two files containing lists of names if given two filenames,
    where each line contains one name.
    Or if none given, takes input from the user.
    """

    if len(sys.argv) == 3:
        pd1 = read_names(sys.argv[1])
        pd2 = read_names(sys.argv[2])
    elif len(sys.argv) == 1:
        pd1, pd2 = addToList()
    else:
        print("Usage: python names.py for manual user input. Enter \'exit\' for period number in order to stop input")
        print("Usage: python names.py pd1_filename pd2_filename for textfile name entry")
        return

    # Creates dictionary as prescribed, then a list of all the names
    name_dict = {1: pd1, 2: pd2}
    all = name_dict[1] + name_dict[2]


    # Pick a random name from the list of pd1 and pd2 names
    name_index = randrange(len(all))
    print(all[name_index])

if __name__ == "__main__":
    main()
