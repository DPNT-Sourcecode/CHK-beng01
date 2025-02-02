from checkout_solution import checkout
from checkout_solution import count_letters

"""
Our price table and offers: 
+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
| F    | 10    | 2F get one F free      |
| G    | 20    |                        |
| H    | 10    | 5H for 45, 10H for 80  |
| I    | 35    |                        |
| J    | 60    |                        |
| K    | 80    | 2K for 150             |
| L    | 90    |                        |
| M    | 15    |                        |
| N    | 40    | 3N get one M free      |
| O    | 10    |                        |
| P    | 50    | 5P for 200             |
| Q    | 30    | 3Q for 80              |
| R    | 50    | 3R get one Q free      |
| S    | 30    |                        |
| T    | 20    |                        |
| U    | 40    | 3U get one U free      |
| V    | 50    | 2V for 90, 3V for 130  |
| W    | 20    |                        |
| X    | 90    |                        |
| Y    | 10    |                        |
| Z    | 50    |                        |
+------+-------+------------------------+
"""

def run_test_cases():
    test_cases = [
        ("AABBCD", 180),
        ("AAAAA", 200),
        ("EEEEBB", 160),
        ("EEEBBB", 165),
        ("ABCDX", 205),  # Invalid case
        ("FFFFFF", 40),
        ("FFFFF", 40),
        ("FFF", 20),
        ("NNNM", 120),
        ("RRRQ", 150),
        ("UUUU", 120),
        ("PPPPP", 200),
        ("QQQ", 80),
        ("VVV", 130),
        ("VV", 90),
        ("HHHHH", 45),
        ("HHHHHHHHHH", 80),
        ("HHHHHHHHHHH", 90),
    ]

    for skus, expected in test_cases:
        actual = checkout(skus)
        result = "✅ PASSED" if actual == expected else f"❌ FAILED (Expected: {expected}, Got: {actual})"
        print(f"checkout({skus}) -> {actual} | {result}")

# Run all test cases
run_test_cases()




