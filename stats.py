letter = {}

def sort_on(dict):
    try:
        return dict["num"]
    except Exception as e:
        print('')


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
    list = []
    for char, num in dict.items():
        list.append({"char": char, "num": num})
    list.sort(reverse=True, key=sort_on)
    print("--------- Character Count -------")
    for i in range(0, len(list)):
        print(f"{list[i]['char']}: {list[i]['num']}")
    print("============= END ===============")

