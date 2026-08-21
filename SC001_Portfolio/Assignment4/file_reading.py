"""
File: file_reading.py
Name: Summer
---------------------------------
This program reads input from a file named "data.txt" and
processes each line to extract all numerical digits.

After collecting the digits, the program calculates the
maximum, minimum, and average values, and displays the
results on the console.
"""


FILE = 'data.txt'
FILE1 = 'data_1.txt'


def main():
    """
    Read valid numbers from the file and compute their max, min, and average, excepting "Nan".
    """
    with open(FILE, "r") as f:
        max_s = -float("inf")
        min_s = float("inf")
        total = 0
        count = 0
        for line in f:
            if line != "Nan\n":
                data = float(line)
                if data > max_s:
                    max_s = data
                if data < min_s:
                    min_s = data
                total += data
                count += 1
        if count == 0:
            print("No data in this file.")
        else:
            print("Max: "+str(max_s))
            print("Min: "+str(min_s))
            print("Avg: "+str(total/count))


if __name__ == '__main__':
    main()
