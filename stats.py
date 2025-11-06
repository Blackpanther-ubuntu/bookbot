def num_words(filepath):
    with open(filepath) as f:
        contents = f.read()
        words = contents.split()
        len_words = len(words)
        print(f"Found {len_words} total words")