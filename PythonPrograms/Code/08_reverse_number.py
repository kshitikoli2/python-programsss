# Program 8: Reverse a Number


def reverse_number(n):
    """Reverse the digits of an integer. Keeps the sign (-123 -> -321)."""
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return sign * reversed_num


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Reversed number:", reverse_number(num))
