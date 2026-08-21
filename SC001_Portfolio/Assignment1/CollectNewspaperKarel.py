"""
File: CollectNewspaperKarel.py
Name: Summer
--------------------------------
At the start, this program does nothing.

Your task is to add the necessary code
to guide Karel to walk to the door of its house,
pick up the newspaper (represented by a beeper),
and then return to its original position
in the upper-left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition:at (3,4) facing east
    post-condition:on beeper at (3,4) facing east
    """
    move_to_b()
    back_to_o()
    put_beeper()


def move_to_b():
    """
    pre-condition:at (3,4) facing east
    post-condition:on beeper facing east
    """
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()


def back_to_o():
    """
    pre-condition:on beeper facing east
    post-condition:at (3,4) facing east
    """
    pick_beeper()
    turn_left()
    turn_left()
    move_three()
    turn_right()
    move()
    turn_right()


def turn_right():
    for i in range(3):
        turn_left()


def move_three():
    for i in range(3):
        move()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
