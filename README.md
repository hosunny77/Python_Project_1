# SC001 Python Project

A collection of Python assignments completed for **stanCode SC001**, a course adapted from Stanford's CS106A. Each assignment applies a different set of core Python concepts, from control flow to file I/O and image processing.

## Assignment 1 — Karel the Robot
**Concepts:** control flow, `while` loops, conditionals, function decomposition

Karel the Robot is programmed using only movement/sensing commands (`move`, `turn_left`, `put_beeper`, `front_is_clear`, etc.) to solve four grid-based tasks.

- `CheckerboardKarel.py` — Fills the world with beepers in a checkerboard pattern, one row at a time.
- `CollectNewspaperKarel.py` — Walks Karel to the door of its house, picks up the "newspaper" (a beeper), and returns to its starting position.
- `MidpointKarel.py` — Locates the corner closest to the midpoint of 1st Street and marks it with a beeper, using temporary beepers to search without leaving traces behind.
- `StoneMasonKarel.py` — Builds equal-height (5-beeper) stone pillars on each avenue across the world.

## Assignment 2 — Numbers & Loops
**Concepts:** `while` loops, arithmetic operators, string formatting, user input handling

- `hailstone.py` — Simulates the Hailstone (Collatz) sequence for a user-given number (applying n/2 or 3n+1 until it reaches 1) and reports the number of steps taken.
- `prime_checker.py` — Repeatedly asks for an integer and determines whether it's prime by testing divisibility.
- `quadratic_solver.py` — Solves ax² + bx + c = 0 for user-given a, b, c, handling two real roots, one root, or no real roots based on the discriminant.
- `weather_master.py` — Reads a stream of temperature readings until a sentinel value is entered, then reports the highest, lowest, and average temperature, plus the number of "cold days" (< 16°).

## Assignment 3 — String Manipulation
**Concepts:** string indexing/slicing, iteration, algorithm design

- `caesar.py` — Encrypts/decrypts text using a Caesar cipher shift determined by a user-provided secret number.
- `complement.py` — Builds the complementary DNA strand for a given sequence (A↔T, G↔C).
- `hangman.py` — A console Hangman game where the player guesses letters to reveal a randomly chosen word within a limited number of wrong guesses.
- `rocket.py` — Draws an ASCII-art rocket whose size scales with a constant.
- `extension_similarity.py` — Compares a short DNA sequence against every subsequence of a longer one to find the closest match, based on character-by-character similarity scoring.

## Assignment 4 — Files & Images
**Concepts:** file I/O, 2D pixel iteration, nested loops, third-party libraries (Pillow)

- `file_reading.py` — Reads numeric data from a text file (skipping "Nan" entries) and computes the max, min, and average.
- `fire.py` — Scans an image pixel by pixel, highlighting areas where the red channel stands out (fire) in red and converting the rest to grayscale.
- `mirror_lake.py` — Generates a "reflection" effect by placing a vertically flipped copy of an image directly below the original.
- `python_random_generator.py` — Simulates repeated die rolls and counts how many "runs" (immediate repeats of the same value) occur.

## Notes
- `karel/` (Assignment 1) and `simpleimage.py` (Assignment 4) are course-provided support libraries, not original work.
- Requires Python 3 and [Pillow](https://pypi.org/project/Pillow/) (`pip install pillow`) for Assignment 4.
