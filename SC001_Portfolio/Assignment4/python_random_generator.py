"""
File: python_random_generator.py
Name: Summer
-----------------------------
This program simulates a given number of die rolls and
analyzes the results to determine how many consecutive
numbers appear, which are defined as runs.
"""


import random


NUM_ROLLS = 15


def main():
    """
    Count how many runs of consecutive numbers appear.
    If more than two consecutive rolls are the same only count once for consecutive duplicates.
    """
    r1 = random.randint(1, 6)
    print("Rolls: " + str(r1))
    run = 0
    can_add = True
    for i in range(NUM_ROLLS-1):
        r2 = random.randint(1, 6)
        print("Rolls: " + str(r2))
        if r1 == r2:
            if can_add:
                run += 1
                can_add = False
        else:
            can_add = True
        r1 = r2
    print('Number of runs: '+str(run))


if __name__ == '__main__':
    main()
