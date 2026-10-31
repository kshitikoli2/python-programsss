import importlib.util
from pathlib import Path

# Load Code/08_reverse_number.py
_path = Path(__file__).resolve().parent.parent / "Code" / "08_reverse_number.py"
_spec = importlib.util.spec_from_file_location("reverse_number", _path)
program = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(program)


def test_reverse_number():
    assert program.reverse_number(123) == 321
    assert program.reverse_number(1200) == 21
    assert program.reverse_number(7) == 7
    assert program.reverse_number(0) == 0
    assert program.reverse_number(-456) == -654


if __name__ == "__main__":
    test_reverse_number()
    print("All test cases passed.")
