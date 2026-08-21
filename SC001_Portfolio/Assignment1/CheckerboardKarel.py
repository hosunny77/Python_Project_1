"""
File: CheckerboardKarel.py
Name: Summer
----------------------------
When finished, this program should
draw a checkerboard pattern using
beepers, as described in Assignment 1.

The solution should work correctly
for all of the sample worlds provided
in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition:at (1,1) facing east
    post-condition:at the either left or right point of northernmost avenue
    with all beepers putting like Checkerboard
    """
    while left_is_clear():
        fill_row()
        up1()
        if left_is_clear():
            fill_row()
            up2()
    fill_row()


def up1():
    """
    pre-condition:at the end of the street facing east
    post-condition:at one right move away from the start point of upper street facing east
    """
    turn_around()
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    move()


def up2():
    """
    pre-condition:at the end of the street facing east
    post-condition:at the start point of upper street facing east
    """
    turn_around()
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_right()


def fill_row():
    # put a beeper and left a blank on the street repeatedly
    while front_is_clear():
        put_beeper()
        move()
        if front_is_clear():
            move()
    step_back_check()


def step_back_check():
    # make sure the end of the street follow the 'put a beeper and left a blank' law
    turn_around()
    move()
    if on_beeper():
        turn_around()
        move()
    else:
        turn_around()
        move()
        put_beeper()


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
