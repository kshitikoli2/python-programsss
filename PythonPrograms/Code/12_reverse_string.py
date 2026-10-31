# Program 12: Reverse a String Without Using Slicing


def reverse_string(text):
    """Reverse a string using a loop."""
    result = ""
    for ch in text:
        result = ch + result
    return result


if __name__ == "__main__":
    text = input("Enter a string: ")
    print("Reversed string:", reverse_string(text))
