import importlib.util
from pathlib import Path

# Load Code/12_reverse_string.py
_path = Path(__file__).resolve().parent.parent / "Code" / "12_reverse_string.py"
_spec = importlib.util.spec_from_file_location("reverse_string", _path)
program = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(program)


def test_reverse_string():
    assert program.reverse_string("hello") == "olleh"
    assert program.reverse_string("Python") == "nohtyP"
    assert program.reverse_string("a") == "a"
    assert program.reverse_string("") == ""
    assert program.reverse_string("ab cd") == "dc ba"


def test_no_slicing_used():
    # The program must not use [::-1]
    source = _path.read_text()
    assert "[::-1]" not in source


if __name__ == "__main__":
    test_reverse_string()
    test_no_slicing_used()
    print("All test cases passed.")
