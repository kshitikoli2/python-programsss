import importlib.util
from pathlib import Path

# Load Code/13_palindrome_string.py
_path = Path(__file__).resolve().parent.parent / "Code" / "13_palindrome_string.py"
_spec = importlib.util.spec_from_file_location("palindrome_string", _path)
program = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(program)


def test_palindrome_string():
    assert program.is_palindrome_string("madam") is True
    assert program.is_palindrome_string("Racecar") is True
    assert program.is_palindrome_string("A man, a plan, a canal: Panama") is True
    assert program.is_palindrome_string("") is True
    assert program.is_palindrome_string("hello") is False
    assert program.is_palindrome_string("Python") is False


if __name__ == "__main__":
    test_palindrome_string()
    print("All test cases passed.")
