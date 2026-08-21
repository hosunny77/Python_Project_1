"""
File: StoneMasonKarel.py
Name: Summer
--------------------------------
At the start, this program does nothing.

Your task is to add the necessary code to guide Karel
to build stone columns that are five beepers tall
on each appropriate avenue, as described in Assignment 1.

Karel should finish on the last avenue at 1st Street, facing east.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition:at (1,1) facing east
    post-condition:at the end of street 1 facing east with all beepers on pillars
    """
    walk_l()
    while front_is_clear():
        move_four()
        walk_l()


def walk_l():
    """
    pre-condition:at the lowest place of pillar facing east
    post-condition:at the lowest place of pillar facing east with all beepers on the pillar
    """
    turn_left()
    put_all_b()
    turn_right()
    turn_right()
    move_four()
    turn_left()


def put_all_b():
    """
    pre-condition:at the lowest place of pillar facing north
    post-condition:at the highest place of pillar facing north with all beepers on the pillar
    """
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
    if not on_beeper():
        put_beeper()


def turn_right():
    for i in range(3):
        turn_left()


def move_four():
    for i in range(4):
        move()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
