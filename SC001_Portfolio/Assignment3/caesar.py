"""
File: caesar.py
Name: Summer
------------------------------
This program demonstrates the idea of the Caesar cipher.

The user is first asked to enter a number that determines
how much the alphabet should be shifted to form a cipher
table. After that, any input string will be encrypted
using the generated cipher.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    Decipher a Caesar code using a secret number.
    """
    secret = int(input("Secret Number: "))
    new_alphabet = get_new_alphabet(secret)
    cipher = input("What's the ciphered string?")
    result = decipher(cipher, new_alphabet)
    print("The deciphered string is: "+result)


def decipher(cipher, new_alphabet):
    ans = ""
    for ch in cipher:
        if ch.isupper():
            i = new_alphabet.find(ch)
            ans += ALPHABET[i]
        elif ch.islower():
            s = ch.upper()
            i = new_alphabet.find(s)
            ans += ALPHABET[i]
        else:
            ans += ch
    return ans


def get_new_alphabet(secret):
    first = ALPHABET[26-secret:]
    second = ALPHABET[:26-secret]
    return first + second


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == '__main__':
    main()
