# Program 4: Calculate Factorial


def factorial(n):
    """Return n! for a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    num = int(input("Enter a non-negative number: "))
    print(f"Factorial of {num} is {factorial(num)}")
