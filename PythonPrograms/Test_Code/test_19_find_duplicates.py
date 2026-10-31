import importlib.util
from pathlib import Path

# Load Code/19_find_duplicates.py
_path = Path(__file__).resolve().parent.parent / "Code" / "19_find_duplicates.py"
_spec = importlib.util.spec_from_file_location("find_duplicates", _path)
program = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(program)


def test_find_duplicates():
    assert program.find_duplicates([1, 2, 3, 2, 4, 1]) == [2, 1]
    assert program.find_duplicates([1, 2, 3]) == []
    assert program.find_duplicates([5, 5, 5, 5]) == [5]
    assert program.find_duplicates([]) == []
    assert program.find_duplicates(["a", "b", "a", "c", "b"]) == ["a", "b"]


if __name__ == "__main__":
    test_find_duplicates()
    print("All test cases passed.")
