# Program 2: Find Largest of Three Numbers


def largest_of_three(a, b, c):
    """Return the largest of three numbers (without using max)."""
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    return c


if __name__ == "__main__":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))
    print("Largest number is:", largest_of_three(a, b, c))
