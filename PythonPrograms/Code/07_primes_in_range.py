# Program 7: Print Prime Numbers in a Range


def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def primes_in_range(start, end):
    """Return all prime numbers from start to end (both inclusive)."""
    return [n for n in range(start, end + 1) if is_prime(n)]


if __name__ == "__main__":
    start = int(input("Enter start: "))
    end = int(input("Enter end: "))
    print(f"Primes between {start} and {end}:", primes_in_range(start, end))
