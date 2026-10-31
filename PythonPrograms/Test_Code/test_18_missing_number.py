import importlib.util
from pathlib import Path

# Load Code/18_missing_number.py
_path = Path(__file__).resolve().parent.parent / "Code" / "18_missing_number.py"
_spec = importlib.util.spec_from_file_location("missing_number", _path)
program = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(program)


def test_missing_number():
    assert program.missing_number([1, 2, 4, 5, 6]) == 3
    assert program.missing_number([2, 3, 4, 5]) == 1
    assert program.missing_number([1, 2, 3, 4]) == 5
    assert program.missing_number([5, 3, 1, 2]) == 4
    assert program.missing_number([]) == 1


if __name__ == "__main__":
    test_missing_number()
    print("All test cases passed.")
