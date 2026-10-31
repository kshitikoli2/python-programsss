import importlib.util
from pathlib import Path

# Load Code/16_remove_duplicates.py
_path = Path(__file__).resolve().parent.parent / "Code" / "16_remove_duplicates.py"
_spec = importlib.util.spec_from_file_location("remove_duplicates", _path)
program = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(program)


def test_remove_duplicates():
    assert program.remove_duplicates([1, 2, 2, 3, 1, 4]) == [1, 2, 3, 4]
    assert program.remove_duplicates([5, 5, 5]) == [5]
    assert program.remove_duplicates([]) == []
    assert program.remove_duplicates([1, 2, 3]) == [1, 2, 3]
    assert program.remove_duplicates(["a", "b", "a"]) == ["a", "b"]


if __name__ == "__main__":
    test_remove_duplicates()
    print("All test cases passed.")
