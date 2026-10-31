import importlib.util
from pathlib import Path

# Load Code/04_factorial.py
_path = Path(__file__).resolve().parent.parent / "Code" / "04_factorial.py"
_spec = importlib.util.spec_from_file_location("factorial", _path)
program = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(program)


def test_factorial():
    assert program.factorial(0) == 1
    assert program.factorial(1) == 1
    assert program.factorial(5) == 120
    assert program.factorial(7) == 5040
    assert program.factorial(10) == 3628800

    # Negative numbers should raise ValueError
    try:
        program.factorial(-3)
        assert False, "Expected ValueError for negative input"
    except ValueError:
        pass


if __name__ == "__main__":
    test_factorial()
    print("All test cases passed.")
