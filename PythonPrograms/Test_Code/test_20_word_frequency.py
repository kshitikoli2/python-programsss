import importlib.util
from pathlib import Path

# Load Code/20_word_frequency.py
_path = Path(__file__).resolve().parent.parent / "Code" / "20_word_frequency.py"
_spec = importlib.util.spec_from_file_location("word_frequency", _path)
program = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(program)


def test_word_frequency():
    assert program.word_frequency("the cat and the hat") == {"the": 2, "cat": 1, "and": 1, "hat": 1}
    assert program.word_frequency("Hello hello HELLO") == {"hello": 3}
    assert program.word_frequency("Hi, there! Hi.") == {"hi": 2, "there": 1}
    assert program.word_frequency("") == {}
    assert program.word_frequency("one") == {"one": 1}


if __name__ == "__main__":
    test_word_frequency()
    print("All test cases passed.")
