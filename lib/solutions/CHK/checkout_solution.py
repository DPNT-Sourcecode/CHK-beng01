from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    counts = count_letters(skus)

def count_letters(s: str):
    counts = Counter(s)  # Count occurrences of each character
    return {letter: counts[letter] for letter in "ABCD"}  # Return only counts of A, B, C, and D


"""
+------+-------+----------------+
| Item | Price | Special offers |
+------+-------+----------------+
| A    | 50    | 3A for 130     |
| B    | 30    | 2B for 45      |
| C    | 20    |                |
| D    | 15    |                |
+------+-------+----------------+ 
"""


