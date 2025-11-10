letter = {}

def sort_on(letters):
    return[letters.key]

def num_words(filepath):
    with open(filepath) as f:
        contents = f.read()
        words = contents.split()
        len_words = len(words)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {len_words} total words")

def num_characters(filepath, dict):
    with open(filepath) as f:
        contents = f.read()
        length = len(contents)
        for i in range(0, length):
            if contents[i].lower() in dict and contents[i].isalpha():
                f = contents[i].lower()
                dict[f"{f}"] = dict[f"{f}"] + 1
            if contents[i].lower() not in dict and contents[i].isalpha():
                t = contents[i].lower()
                dict[f"{t}"] = 1
        #print(dict)

def sorted_characters(dict):
    list1 = list(dict.items())
    list2 = sorted(list1, reverse=True, key=sort_on)
    print(list2)


def main():
    num_characters("books/frankenstein.txt", letter)
    sorted_characters(letter)

main()