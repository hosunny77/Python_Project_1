"""
File: similarity.py (extension)
Name: Summer
----------------------------
This program is an extension of Assignment 3.

It compares a short DNA sequence, s2, with all possible
subsequences of a longer DNA sequence, s1. The approach
used in this program is similar to the techniques commonly
applied in the bioinformatics industry.
"""


def main():
    """
    Pre-condition:The user provides two DNA sequences to compare.
    Post-condition:Find out the highest similarity sequence between two sequences.
    """
    s1 = input("Please give me a DNA sequence to search: ")
    s2 = input("What DNA sequence would you like to match? ")
    s1 = s1.upper()
    s2 = s2.upper()
    best_match = find_best_match(s1, s2)
    print("The best match is "+best_match)


def find_best_match(long, short):
    best_match = ""
    best_score = 0
    for i in range(len(long) - len(short) + 1):
        piece = long[i:i + len(short)]
        score = similarity(piece, short)
        if score >= best_score:
            best_score = score
            best_match = piece
    return best_match


def similarity(piece, short):
    count = 0
    for i in range(len(short)):
        if piece[i] == short[i]:
            count += 1
    return count


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == '__main__':
    main()
