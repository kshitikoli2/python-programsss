import importlib.util
from pathlib import Path

# Load Code/09_palindrome_number.py
_path = Path(__file__).resolve().parent.parent / "Code" / "09_palindrome_number.py"
_spec = importlib.util.spec_from_file_location("palindrome_number", _path)
program = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(program)


def test_palindrome_number():
    assert program.is_palindrome_number(121) is True
    assert program.is_palindrome_number(1221) is True
    assert program.is_palindrome_number(7) is True
    assert program.is_palindrome_number(0) is True
    assert program.is_palindrome_number(123) is False
    assert program.is_palindrome_number(10) is False
    assert program.is_palindrome_number(-121) is False


if __name__ == "__main__":
    test_palindrome_number()
    print("All test cases passed.")
