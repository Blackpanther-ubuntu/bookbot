import sys
from stats import num_words
from stats import num_characters
from stats import sorted_characters
try:
    input = sys.argv[1]
except IndexError as i:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
letters = {}

def main():
    num_words(input)
    num_characters(input, letters)
    sorted_characters(letters)

main()