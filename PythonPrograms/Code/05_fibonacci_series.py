# Program 5: Generate Fibonacci Series


def fibonacci_series(n):
    """Return a list with the first n Fibonacci numbers."""
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


if __name__ == "__main__":
    terms = int(input("How many terms? "))
    print("Fibonacci series:", fibonacci_series(terms))
