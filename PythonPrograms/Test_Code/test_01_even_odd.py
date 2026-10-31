import importlib.util
from pathlib import Path

# Load Code/01_even_odd.py (file names starting with a number can't be imported normally)
_path = Path(__file__).resolve().parent.parent / "Code" / "01_even_odd.py"
_spec = importlib.util.spec_from_file_location("even_odd", _path)
program = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(program)


def test_even_odd():
    assert program.even_or_odd(4) == "Even"
    assert program.even_or_odd(7) == "Odd"
    assert program.even_or_odd(0) == "Even"
    assert program.even_or_odd(-3) == "Odd"
    assert program.even_or_odd(-10) == "Even"


if __name__ == "__main__":
    test_even_odd()
    print("All test cases passed.")
