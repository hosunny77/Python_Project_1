"""
File: weather_master.py
Name: Summer
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant controls when to stop
EXIT = -100


def main():
	"""
	The program find out the highest temperature, lowest temperature, average temperature,
	and the number of cold days (temperatures < 16 degrees).
	"""
	print("stanCode \"Weather Master 4.0\"!")
	data = int(input("Next Temperature: (or " + str(EXIT) + " to quit)?"))
	if data == EXIT:
		print("No temperatures were entered.")
		return

	maximum = data
	minimum = data
	total = data
	count = 1
	cold_days = 0
	if data < 16:
		cold_days += 1

	while True:
		data = int(input("Next Temperature: (or " + str(EXIT) + " to quit)?"))
		if data == EXIT:
			break
		if data > maximum:
			maximum = data
		if data < minimum:
			minimum = data

		count += 1
		total += data
		if data < 16:
			cold_days += 1

	print("Highest temperature = " + str(maximum))
	print("Lowest temperature = " + str(minimum))
	print("Average = " + str(total / count))
	print(str(cold_days) + ' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == "__main__":
	main()
