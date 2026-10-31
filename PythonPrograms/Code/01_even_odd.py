# Program 1: Check Even or Odd


def even_or_odd(n):
    """Return 'Even' if n is even, otherwise 'Odd'."""
    if n % 2 == 0:
        return "Even"
    return "Odd"


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"{num} is {even_or_odd(num)}")
