import importlib.util
from pathlib import Path

# Load Code/14_char_frequency.py
_path = Path(__file__).resolve().parent.parent / "Code" / "14_char_frequency.py"
_spec = importlib.util.spec_from_file_location("char_frequency", _path)
program = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(program)


def test_char_frequency():
    assert program.char_frequency("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
    assert program.char_frequency("aaa") == {"a": 3}
    assert program.char_frequency("") == {}
    assert program.char_frequency("a b") == {"a": 1, " ": 1, "b": 1}
    assert program.char_frequency("Aa") == {"A": 1, "a": 1}


if __name__ == "__main__":
    test_char_frequency()
    print("All test cases passed.")
