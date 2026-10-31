# Program 13: Check Palindrome String


def is_palindrome_string(text):
    """Return True if text is a palindrome.
    Ignores case, spaces and punctuation."""
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    text = input("Enter a string: ")
    if is_palindrome_string(text):
        print(f'"{text}" is a palindrome')
    else:
        print(f'"{text}" is not a palindrome')
