"""
File: hailstone.py
Name: Summer
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    Computes the Hailstone sequence for a positive integer
    until it reaches 1, and reports the total number of steps.
    """
    print("This program computes Hailstone sequences")
    print("")
    n = int(input("Enter a number"))
    count = 0
    while n != 1:
        if n % 2 == 1:
            print(str(n)+" is odd, so I make 3n+1: "+str(3*n+1))
            n = 3 * n + 1
        else:
            print(str(n) + " is even, so I take half: " + str(n//2))
            n = n // 2
        count += 1
    print("It took "+str(count)+" steps to reach 1.")


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == "__main__":
    main()
