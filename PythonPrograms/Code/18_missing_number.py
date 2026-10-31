# Program 18: Find Missing Number in a List
# The list contains numbers from 1 to n with exactly one number missing.


def missing_number(numbers):
    """Return the missing number from a list of 1..n."""
    n = len(numbers) + 1
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(numbers)


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Missing number:", missing_number(numbers))
