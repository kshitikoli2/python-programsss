# Program 3: Check Positive, Negative, or Zero


def check_number(n):
    """Return 'Positive', 'Negative' or 'Zero'."""
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    return "Zero"


if __name__ == "__main__":
    num = float(input("Enter a number: "))
    print(f"{num} is {check_number(num)}")
