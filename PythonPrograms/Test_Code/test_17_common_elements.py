import importlib.util
from pathlib import Path

# Load Code/17_common_elements.py
_path = Path(__file__).resolve().parent.parent / "Code" / "17_common_elements.py"
_spec = importlib.util.spec_from_file_location("common_elements", _path)
program = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(program)


def test_common_elements():
    assert program.common_elements([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]
    assert program.common_elements([1, 2], [3, 4]) == []
    assert program.common_elements([1, 1, 2], [1, 2, 2]) == [1, 2]
    assert program.common_elements([], [1, 2]) == []
    assert program.common_elements(["a", "b"], ["b", "c"]) == ["b"]


if __name__ == "__main__":
    test_common_elements()
    print("All test cases passed.")
