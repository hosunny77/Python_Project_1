"""
File: MidpointKarel.py
Name: Summer
----------------------------
When finished, this program should leave a beeper
on the corner closest to the midpoint of 1st Street.

If 1st Street has an even number of corners,
either of the two central corners is acceptable.
Karel may use additional beepers while searching
for the midpoint, but must remove them before stopping.

The world can be of any size, and you may assume
that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition:at (1,1) facing east
    post-condition:at the midpoint of street 1 and on the beeper
    """
    fill_row()
    remove_point()
    while on_beeper():
        get_midpoint()
    put_beeper()


def fill_row():
    """
    pre-condition:at (1,1) facing east
    post-condition:fill beepers on street 1
    """
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()


def remove_point():
    """
    pre-condition:at the end of street 1 facing east with beepers fill street 1
    post-condition:at (1,2) of street 1 facing east on beeper
    with beepers fill street 1 but the two points of the street 1
    """
    pick_beeper()
    turn_around()
    while front_is_clear():
        move()
    pick_beeper()
    turn_around()
    move()


def get_midpoint():
    """
    pre-condition:at (1,2) of street 1 facing east on beeper
    with beepers fill street 1 but the two points of the street 1
    post-condition:at the midpoint of street 1
    """
    while on_beeper():
        pick_beeper()
        move()
        while on_beeper():
            move()
        turn_around()
        move()


def turn_around():
    turn_left()
    turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
