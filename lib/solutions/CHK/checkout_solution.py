from collections import Counter

"""
+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
| F    | 10    | 2F get one F free      |
+------+-------+------------------------+
"""

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    counts = count_letters(skus)
    if counts.get("invalid", 0) > 0: return -1
    apply_free_B_from_E(counts)
    apply_free_F_offer(counts)
    return (
        calculateA(counts.get('A', 0)) + 
        calculateB(counts.get('B', 0)) + 
        calculateC(counts.get('C', 0)) + 
        calculateD(counts.get('D', 0)) + 
        calculateE(counts.get('E', 0)) + 
        calculateF(counts.get('F', 0)
    )
                                                                                                                                                                             )


def count_letters(s: str):
    counts = Counter(s)  # Count occurrences of all characters
    valid_letters = "ABCDE"
    
    # Extract counts for 'A', 'B', 'C', 'D'
    result = {letter: counts[letter] for letter in valid_letters}
    
    # Count invalid characters
    invalid_count = sum(counts[char] for char in counts if char not in valid_letters)
    
    # Add invalid count to the result
    result["invalid"] = invalid_count

    return result

def calculateA(count: int):
    price = 50
    price_3A = 130  # 3A for 130
    price_5A = 200  # 5A for 200
    
    sets_of_5 = count // 5
    remaining_after_5 = count % 5
    sets_of_3 = remaining_after_5 // 3
    remaining_after_3 = remaining_after_5 % 3

    total_cost = (sets_of_5 * price_5A) + (sets_of_3 * price_3A) + (remaining_after_3 * price)
    return total_cost

def calculateB(count: int):
    cost_per_apple = 30
    discount_price = 45  # Cost for 3 apples
    discount_quantity = 2

    # Calculate cost using discount for every set of 3 apples
    sets_of_two = count // discount_quantity
    remaining_apples = count % discount_quantity

    total_cost = (sets_of_two * discount_price) + (remaining_apples * cost_per_apple)
    return total_cost

def calculateC(count: int):
    return count * 20

def calculateD(count: int):
    return count * 15

def calculateE(count: int):
    return count * 40

def calculateF(count: int):
    return count * 10

def apply_free_B_from_E(counts):
    """ Apply the special offer: Buy 2 E, get 1 B free """
    if 'E' in counts and 'B' in counts:
        free_B_count = counts['E'] // 2  # One free B for every 2 Es
        counts['B'] = max(0, counts['B'] - free_B_count)  # Reduce B count to reflect free Bs

def apply_free_F_offer(counts):
    """ Apply the special offer: Buy 2 F, get 1 F free """
    if 'F' in counts:
        free_F_count = counts['F'] // 3  # One free F for every 3 Fs
        counts['F'] -= free_F_count  # Reduce count to reflect the free items

