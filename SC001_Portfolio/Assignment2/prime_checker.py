"""
File: prime_checker.py
Name: Summer
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""


# This constant controls when to stop
EXIT = -100


def main():
	"""
	Check whether an integer >1 is a prime number.
	"""
	print("Welcome to the prime checker!")
	while True:
		n = int(input("n: "))
		if n == EXIT:
			print("Have a good one!")
			return
		start = 2
		while start != n:
			if n % start == 0:
				print(str(n)+' is not a prime number.')
				break
			else:
				start += 1
		if start == n:
			print(str(n)+' is a prime number.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
