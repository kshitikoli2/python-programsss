import importlib.util
from pathlib import Path

# Load Code/11_vowels_consonants.py
_path = Path(__file__).resolve().parent.parent / "Code" / "11_vowels_consonants.py"
_spec = importlib.util.spec_from_file_location("vowels_consonants", _path)
program = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(program)


def test_vowels_consonants():
    assert program.count_vowels_consonants("hello") == (2, 3)
    assert program.count_vowels_consonants("Python") == (1, 5)
    assert program.count_vowels_consonants("AEIOU") == (5, 0)
    assert program.count_vowels_consonants("Hello World 123!") == (3, 7)
    assert program.count_vowels_consonants("") == (0, 0)


if __name__ == "__main__":
    test_vowels_consonants()
    print("All test cases passed.")
