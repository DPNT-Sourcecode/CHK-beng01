from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    counts = count_letters(skus)
    
    # If there are invalid characters, return -1
    if counts.get("invalid", 0) > 0:
        return -1

    # Apply "Buy X get Y free" offers first before price calculations
    apply_free_B_from_E(counts)
    apply_free_F_offer(counts)
    apply_free_M_from_N(counts)
    apply_free_Q_from_R(counts)
    apply_free_U_offer(counts)

    # Apply group discount (S, T, X, Y, Z)
    group_discount_total = apply_group_discount(counts)

    # Calculate total cost after group discount
    total_cost = sum(calculate_price(item, count) for item, count in counts.items() if item != "invalid")
    
    return total_cost + group_discount_total

def count_letters(s: str):
    counts = Counter(s)  # Count occurrences of all characters
    valid_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Extract counts for valid items
    result = {letter: counts[letter] for letter in valid_letters}
    
    # Count invalid characters
    invalid_count = sum(counts[char] for char in counts if char not in valid_letters)
    
    # Add invalid count to the result
    result["invalid"] = invalid_count

    return result

### ***FREE ITEM OFFERS (Handled before price calculations)***

def apply_free_B_from_E(counts):
    """ Apply the special offer: Buy 2E, get 1B free """
    if 'E' in counts and 'B' in counts:
        free_B_count = counts['E'] // 2  # One free B for every 2 Es
        counts['B'] = max(0, counts['B'] - free_B_count)  # Reduce B count

def apply_free_F_offer(counts):
    """ Apply the special offer: Buy 2F, get 1F free """
    if 'F' in counts:
        free_F_count = counts['F'] // 3  # One free F for every 3 Fs
        counts['F'] -= free_F_count  # Reduce count

def apply_free_M_from_N(counts):
    """ Apply the special offer: Buy 3N, get 1M free """
    if 'N' in counts and 'M' in counts:
        free_M_count = counts['N'] // 3  # One free M for every 3 Ns
        counts['M'] = max(0, counts['M'] - free_M_count)  # Reduce M count

def apply_free_Q_from_R(counts):
    """ Apply the special offer: Buy 3R, get 1Q free """
    if 'R' in counts and 'Q' in counts:
        free_Q_count = counts['R'] // 3  # One free Q for every 3 Rs
        counts['Q'] = max(0, counts['Q'] - free_Q_count)  # Reduce Q count

def apply_free_U_offer(counts):
    """ Apply the special offer: Buy 3U, get 1U free """
    if 'U' in counts:
        free_U_count = counts['U'] // 4  # Every 4U gives 1 free
        counts['U'] -= free_U_count  # Reduce count

### ***GROUP DISCOUNT OFFER***

def apply_group_discount(counts):
    """ Applies the 'buy any 3 of (S, T, X, Y, Z) for 45' offer optimally """
    group_items = ["S", "T", "X", "Y", "Z"]
    group_prices = {"S": 20, "T": 20, "X": 17, "Y": 20, "Z": 21}
    total_group_count = sum(counts[item] for item in group_items if item in counts)
    
    group_discount_total = 0
    while total_group_count >= 3:
        # Apply group discount
        group_discount_total += 45
        total_group_count -= 3
        
        # Reduce the counts optimally (remove the most expensive items first)
        sorted_items = sorted(group_items, key=lambda item: -group_prices[item])
        for item in sorted_items:
            if counts.get(item, 0) > 0:
                counts[item] -= 1
                total_group_count -= 1
                if total_group_count < 3:
                    break
    
    return group_discount_total

### ***PRICE CALCULATION***

def calculate_price(item: str, count: int) -> int:
    """ Calculates the price of an item including any special offers """
    PRICES = {
        "A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10, "G": 20, "H": 10,
        "I": 35, "J": 60, "K": 70, "L": 90, "M": 15, "N": 40, "O": 10, "P": 50,
        "Q": 30, "R": 50, "S": 20, "T": 20, "U": 40, "V": 50, "W": 20, "X": 17,
        "Y": 20, "Z": 21
    }

    DISCOUNTS = {
        "A": [(5, 200), (3, 130)],
        "B": [(2, 45)],
        "H": [(10, 80), (5, 45)],
        "K": [(2, 120)],
        "P": [(5, 200)],
        "Q": [(3, 80)],
        "V": [(3, 130), (2, 90)]
    }

    if item in DISCOUNTS:
        total_cost = 0
        for bundle_size, bundle_price in DISCOUNTS[item]:
            bundles = count // bundle_size
            count %= bundle_size
            total_cost += bundles * bundle_price
        total_cost += count * PRICES[item]
        return total_cost
    else:
        return count * PRICES[item]  # Items without discounts
