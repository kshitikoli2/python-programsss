# Program 14: Count Frequency of Characters


def char_frequency(text):
    """Return a dict with the count of each character."""
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


if __name__ == "__main__":
    text = input("Enter a string: ")
    for ch, count in char_frequency(text).items():
        print(f"'{ch}': {count}")
