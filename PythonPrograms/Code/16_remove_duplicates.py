# Program 16: Remove Duplicates from a List


def remove_duplicates(items):
    """Remove duplicates and keep the original order."""
    result = []
    seen = set()
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


if __name__ == "__main__":
    items = input("Enter items separated by space: ").split()
    print("Without duplicates:", remove_duplicates(items))
