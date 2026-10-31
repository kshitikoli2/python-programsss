# Program 17: Find Common Elements in Two Lists


def common_elements(list1, list2):
    """Return elements present in both lists (no repeats, order of list1)."""
    set2 = set(list2)
    result = []
    for item in list1:
        if item in set2 and item not in result:
            result.append(item)
    return result


if __name__ == "__main__":
    list1 = input("Enter first list (space separated): ").split()
    list2 = input("Enter second list (space separated): ").split()
    print("Common elements:", common_elements(list1, list2))
