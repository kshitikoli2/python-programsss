import importlib.util
from pathlib import Path

# Load Code/06_prime_number.py
_path = Path(__file__).resolve().parent.parent / "Code" / "06_prime_number.py"
_spec = importlib.util.spec_from_file_location("prime_number", _path)
program = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(program)


def test_prime_number():
    assert program.is_prime(2) is True
    assert program.is_prime(3) is True
    assert program.is_prime(17) is True
    assert program.is_prime(97) is True
    assert program.is_prime(1) is False
    assert program.is_prime(0) is False
    assert program.is_prime(-7) is False
    assert program.is_prime(9) is False
    assert program.is_prime(100) is False


if __name__ == "__main__":
    test_prime_number()
    print("All test cases passed.")
