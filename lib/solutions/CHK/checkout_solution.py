from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    counts = count_letters(skus)
    return calculateA(counts.get('A', 0)) + calculateB(counts.get('B', 0)) + calculateC(counts.get('C', 0)) + calculateD(counts.get('D', 0)) 


def count_letters(s: str):
    counts = Counter(s)  # Count occurrences of each character
    return {letter: counts[letter] for letter in "ABCD"}  # Return only counts of A, B, C, and D

def calculateA(count: int):
    cost_per_apple = 50
    discount_price = 130  # Cost for 3 apples
    discount_quantity = 3

    # Calculate cost using discount for every set of 3 apples
    sets_of_three = n // discount_quantity
    remaining_apples = n % discount_quantity

    total_cost = (sets_of_three * discount_price) + (remaining_apples * cost_per_apple)
    return total_cost

def calculateB(count: int):
    cost_per_apple = 30
    discount_price = 45  # Cost for 3 apples
    discount_quantity = 2

    # Calculate cost using discount for every set of 3 apples
    sets_of_two = n // discount_quantity
    remaining_apples = n % discount_quantity

    total_cost = (sets_of_three * discount_price) + (remaining_apples * cost_per_apple)
    return total_cost

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


