"""
File: complement.py
Name: Summer
----------------------------
This program uses string manipulation to solve a real-world
problem: finding the complementary strand of a DNA sequence.

The program provides different DNA sequences as Python strings.
These strings are case-sensitive, and your task is to generate
and output the correct complementary strand for each sequence.
"""


def main():
    """
    Build the complementary DNA strand(A-T,G-C,C-G,T-A).
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    if dna == '':
        return "DNA strand is missing."
    ans = ""
    for i in range(len(dna)):
        if dna[i] == 'A':
            ans = ans + 'T'
        elif dna[i] == 'T':
            ans = ans + 'A'
        elif dna[i] == 'G':
            ans = ans + 'C'
        elif dna[i] == 'C':
            ans = ans + 'G'
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == '__main__':
    main()
