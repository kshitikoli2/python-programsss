import importlib.util
from pathlib import Path

# Load Code/15_second_largest.py
_path = Path(__file__).resolve().parent.parent / "Code" / "15_second_largest.py"
_spec = importlib.util.spec_from_file_location("second_largest", _path)
program = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(program)


def test_second_largest():
    assert program.second_largest([10, 20, 4, 45, 99]) == 45
    assert program.second_largest([5, 5, 4]) == 4
    assert program.second_largest([1, 2]) == 1
    assert program.second_largest([-1, -5, -3]) == -3
    assert program.second_largest([7, 7, 7]) is None
    assert program.second_largest([3]) is None
    assert program.second_largest([]) is None


if __name__ == "__main__":
    test_second_largest()
    print("All test cases passed.")
