def count_words(filename, search_words):
    word_counts = {}

    # Open file and read lines
    with open(filename, 'r') as file:
        lines = file.readlines()

    # word counts for search_words
    for word in search_words:
        word_counts[word] = 0

    # Counting search_words
    for line in lines:
        for word in search_words:
            if word.lower() in line.lower():
                word_counts[word] += 1

    # Print word counts
    for word, count in word_counts.items():
        print("{} -> {}".format(word, count))


filename = "input.txt"
search_words = ["Python", "C", "OOP", "Hello", "Java"]
count_words(filename, search_words)
