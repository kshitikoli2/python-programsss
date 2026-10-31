import importlib.util
from pathlib import Path

# Load Code/10_sum_of_digits.py
_path = Path(__file__).resolve().parent.parent / "Code" / "10_sum_of_digits.py"
_spec = importlib.util.spec_from_file_location("sum_of_digits", _path)
program = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(program)


def test_sum_of_digits():
    assert program.sum_of_digits(123) == 6
    assert program.sum_of_digits(9999) == 36
    assert program.sum_of_digits(0) == 0
    assert program.sum_of_digits(5) == 5
    assert program.sum_of_digits(-482) == 14


if __name__ == "__main__":
    test_sum_of_digits()
    print("All test cases passed.")
