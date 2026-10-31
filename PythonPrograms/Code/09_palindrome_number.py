# Program 9: Check Palindrome Number


def is_palindrome_number(n):
    """Return True if the number reads the same backwards."""
    if n < 0:
        return False
    original = n
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return original == reversed_num


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if is_palindrome_number(num):
        print(f"{num} is a palindrome")
    else:
        print(f"{num} is not a palindrome")
