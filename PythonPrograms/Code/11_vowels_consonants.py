# Program 11: Count Vowels and Consonants


def count_vowels_consonants(text):
    """Return (vowels, consonants). Only letters are counted."""
    vowels = 0
    consonants = 0
    for ch in text.lower():
        if ch.isalpha():
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1
    return vowels, consonants


if __name__ == "__main__":
    text = input("Enter a string: ")
    v, c = count_vowels_consonants(text)
    print("Vowels:", v)
    print("Consonants:", c)
