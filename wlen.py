import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="File path")
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input("Enter the file path: ")

word_length = int(input("Enter length of word: "))

try:
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if len(word) == word_length:
                    print(word)
except FileNotFoundError:
    print("File not found.")