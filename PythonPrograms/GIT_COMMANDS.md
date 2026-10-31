# Git Commands — Assignment 3

## One-time setup
```bash
git clone <YOUR_GITHUB_HTTP_URL>
cd PythonPrograms
git status
```
Copy the `Code/` and `Test_Code/` folders into the cloned `PythonPrograms` folder.

## Run all tests before pushing
```bash
python Test_Code/test_01_even_odd.py
# ...repeat for each test file, or run all at once:
pytest Test_Code -v
```

## Push one file at a time (never `git add .`)

### Program 1 — Even or Odd
```bash
git status
git add Code/01_even_odd.py
git commit -m "Add even odd program"
git push origin main

git status
git add Test_Code/test_01_even_odd.py
git commit -m "Add even odd test cases"
git push origin main
```

### Program 2 — Largest of Three
```bash
git status
git add Code/02_largest_of_three.py
git commit -m "Add largest of three program"
git push origin main

git status
git add Test_Code/test_02_largest_of_three.py
git commit -m "Add largest of three test cases"
git push origin main
```

### Program 3 — Positive, Negative or Zero
```bash
git status
git add Code/03_pos_neg_zero.py
git commit -m "Add positive negative zero program"
git push origin main

git status
git add Test_Code/test_03_pos_neg_zero.py
git commit -m "Add positive negative zero test cases"
git push origin main
```

### Program 4 — Factorial
```bash
git status
git add Code/04_factorial.py
git commit -m "Add factorial program"
git push origin main

git status
git add Test_Code/test_04_factorial.py
git commit -m "Add factorial test cases"
git push origin main
```

### Program 5 — Fibonacci Series
```bash
git status
git add Code/05_fibonacci_series.py
git commit -m "Add fibonacci series program"
git push origin main

git status
git add Test_Code/test_05_fibonacci_series.py
git commit -m "Add fibonacci series test cases"
git push origin main
```

### Program 6 — Prime Number
```bash
git status
git add Code/06_prime_number.py
git commit -m "Add prime number program"
git push origin main

git status
git add Test_Code/test_06_prime_number.py
git commit -m "Add prime number test cases"
git push origin main
```

### Program 7 — Primes in a Range
```bash
git status
git add Code/07_primes_in_range.py
git commit -m "Add primes in range program"
git push origin main

git status
git add Test_Code/test_07_primes_in_range.py
git commit -m "Add primes in range test cases"
git push origin main
```

### Program 8 — Reverse a Number
```bash
git status
git add Code/08_reverse_number.py
git commit -m "Add reverse number program"
git push origin main

git status
git add Test_Code/test_08_reverse_number.py
git commit -m "Add reverse number test cases"
git push origin main
```

### Program 9 — Palindrome Number
```bash
git status
git add Code/09_palindrome_number.py
git commit -m "Add palindrome number program"
git push origin main

git status
git add Test_Code/test_09_palindrome_number.py
git commit -m "Add palindrome number test cases"
git push origin main
```

### Program 10 — Sum of Digits
```bash
git status
git add Code/10_sum_of_digits.py
git commit -m "Add sum of digits program"
git push origin main

git status
git add Test_Code/test_10_sum_of_digits.py
git commit -m "Add sum of digits test cases"
git push origin main
```

### Program 11 — Vowels and Consonants
```bash
git status
git add Code/11_vowels_consonants.py
git commit -m "Add vowels consonants program"
git push origin main

git status
git add Test_Code/test_11_vowels_consonants.py
git commit -m "Add vowels consonants test cases"
git push origin main
```

### Program 12 — Reverse a String
```bash
git status
git add Code/12_reverse_string.py
git commit -m "Add reverse string program"
git push origin main

git status
git add Test_Code/test_12_reverse_string.py
git commit -m "Add reverse string test cases"
git push origin main
```

### Program 13 — Palindrome String
```bash
git status
git add Code/13_palindrome_string.py
git commit -m "Add palindrome string program"
git push origin main

git status
git add Test_Code/test_13_palindrome_string.py
git commit -m "Add palindrome string test cases"
git push origin main
```

### Program 14 — Character Frequency
```bash
git status
git add Code/14_char_frequency.py
git commit -m "Add character frequency program"
git push origin main

git status
git add Test_Code/test_14_char_frequency.py
git commit -m "Add character frequency test cases"
git push origin main
```

### Program 15 — Second Largest
```bash
git status
git add Code/15_second_largest.py
git commit -m "Add second largest program"
git push origin main

git status
git add Test_Code/test_15_second_largest.py
git commit -m "Add second largest test cases"
git push origin main
```

### Program 16 — Remove Duplicates
```bash
git status
git add Code/16_remove_duplicates.py
git commit -m "Add remove duplicates program"
git push origin main

git status
git add Test_Code/test_16_remove_duplicates.py
git commit -m "Add remove duplicates test cases"
git push origin main
```

### Program 17 — Common Elements
```bash
git status
git add Code/17_common_elements.py
git commit -m "Add common elements program"
git push origin main

git status
git add Test_Code/test_17_common_elements.py
git commit -m "Add common elements test cases"
git push origin main
```

### Program 18 — Missing Number
```bash
git status
git add Code/18_missing_number.py
git commit -m "Add missing number program"
git push origin main

git status
git add Test_Code/test_18_missing_number.py
git commit -m "Add missing number test cases"
git push origin main
```

### Program 19 — Find Duplicates
```bash
git status
git add Code/19_find_duplicates.py
git commit -m "Add find duplicates program"
git push origin main

git status
git add Test_Code/test_19_find_duplicates.py
git commit -m "Add find duplicates test cases"
git push origin main
```

### Program 20 — Word Frequency
```bash
git status
git add Code/20_word_frequency.py
git commit -m "Add word frequency program"
git push origin main

git status
git add Test_Code/test_20_word_frequency.py
git commit -m "Add word frequency test cases"
git push origin main
```
