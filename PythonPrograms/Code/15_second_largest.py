# Program 15: Find Second Largest Number in a List


def second_largest(numbers):
    """Return the second largest distinct number, or None if it doesn't exist."""
    first = second = None
    for n in numbers:
        if first is None or n > first:
            second = first
            first = n
        elif n != first and (second is None or n > second):
            second = n
    return second


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Second largest:", second_largest(numbers))
