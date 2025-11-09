from stats import num_words
from stats import num_characters

letters = {}

def main():
    num_words("books/frankenstein.txt")
    num_characters("books/frankenstein.txt", letters)

main()