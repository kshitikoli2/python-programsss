# Program 20: Word Frequency in a Sentence

import string


def word_frequency(sentence):
    """Return a dict with the count of each word (case-insensitive,
    punctuation removed)."""
    cleaned = sentence.lower().translate(str.maketrans("", "", string.punctuation))
    freq = {}
    for word in cleaned.split():
        freq[word] = freq.get(word, 0) + 1
    return freq


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    for word, count in word_frequency(sentence).items():
        print(f"{word}: {count}")
