# Program 19: Find Duplicate Elements in a List


def find_duplicates(items):
    """Return elements that appear more than once (each listed once)."""
    seen = set()
    duplicates = []
    for item in items:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        seen.add(item)
    return duplicates


if __name__ == "__main__":
    items = input("Enter items separated by space: ").split()
    print("Duplicate elements:", find_duplicates(items))
