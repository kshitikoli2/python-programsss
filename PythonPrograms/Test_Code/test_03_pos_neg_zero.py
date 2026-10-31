import importlib.util
from pathlib import Path

# Load Code/03_pos_neg_zero.py
_path = Path(__file__).resolve().parent.parent / "Code" / "03_pos_neg_zero.py"
_spec = importlib.util.spec_from_file_location("pos_neg_zero", _path)
program = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(program)


def test_pos_neg_zero():
    assert program.check_number(5) == "Positive"
    assert program.check_number(-8) == "Negative"
    assert program.check_number(0) == "Zero"
    assert program.check_number(0.5) == "Positive"
    assert program.check_number(-0.1) == "Negative"


if __name__ == "__main__":
    test_pos_neg_zero()
    print("All test cases passed.")
