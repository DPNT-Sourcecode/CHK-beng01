from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    print(type(skus))
    counts = count_letters(skus)
    return calculateA(counts("A")) + calculateB(counts(B)) + calculateC(counts(C)) + calculateD(counts(D)) 


def count_letters(s: str):
    counts = Counter(s)  # Count occurrences of each character
    return {letter: counts[letter] for letter in "ABCD"}  # Return only counts of A, B, C, and D

def calculateA(count: int):
    return count * 50

def calculateB(count: int):
    return count * 30

def calculateC(count: int):
    return count * 20

def calculateD(count: int):
    return count * 15


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
