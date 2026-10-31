import importlib.util
from pathlib import Path

# Load Code/05_fibonacci_series.py
_path = Path(__file__).resolve().parent.parent / "Code" / "05_fibonacci_series.py"
_spec = importlib.util.spec_from_file_location("fibonacci_series", _path)
program = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(program)


def test_fibonacci_series():
    assert program.fibonacci_series(0) == []
    assert program.fibonacci_series(1) == [0]
    assert program.fibonacci_series(2) == [0, 1]
    assert program.fibonacci_series(7) == [0, 1, 1, 2, 3, 5, 8]
    assert program.fibonacci_series(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


if __name__ == "__main__":
    test_fibonacci_series()
    print("All test cases passed.")
