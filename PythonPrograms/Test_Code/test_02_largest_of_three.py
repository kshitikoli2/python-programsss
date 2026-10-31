import importlib.util
from pathlib import Path

# Load Code/02_largest_of_three.py
_path = Path(__file__).resolve().parent.parent / "Code" / "02_largest_of_three.py"
_spec = importlib.util.spec_from_file_location("largest_of_three", _path)
program = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(program)


def test_largest_of_three():
    assert program.largest_of_three(1, 2, 3) == 3
    assert program.largest_of_three(10, 5, 7) == 10
    assert program.largest_of_three(4, 9, 2) == 9
    assert program.largest_of_three(-1, -5, -3) == -1
    assert program.largest_of_three(5, 5, 5) == 5
    assert program.largest_of_three(2.5, 2.7, 1.0) == 2.7


if __name__ == "__main__":
    test_largest_of_three()
    print("All test cases passed.")
