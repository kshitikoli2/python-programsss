import importlib.util
from pathlib import Path

# Load Code/07_primes_in_range.py
_path = Path(__file__).resolve().parent.parent / "Code" / "07_primes_in_range.py"
_spec = importlib.util.spec_from_file_location("primes_in_range", _path)
program = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(program)


def test_primes_in_range():
    assert program.primes_in_range(1, 10) == [2, 3, 5, 7]
    assert program.primes_in_range(10, 20) == [11, 13, 17, 19]
    assert program.primes_in_range(2, 2) == [2]
    assert program.primes_in_range(14, 16) == []
    assert program.primes_in_range(20, 10) == []


if __name__ == "__main__":
    test_primes_in_range()
    print("All test cases passed.")
