from checkout_solution import checkout
from checkout_solution import count_letters

### ***TEST CASES***
def run_formatted_test_cases():
    test_cases = [
        ("STXYZ", 45),     # Group discount applies: 20 + 20 + 17 + 20 + 21 - 21 - 20 - 20 + 45
        ("STXXYZ", 62),    # 45 + 17 (Group discount + 1 extra X)
        ("STXYZXYZ", 90),  # 45 + 45 (Two group discounts)
        ("AAAAA", 200),
        ("EEEEBB", 160),
        ("EEEBBB", 165),
        ("FFFFFF", 40),
        ("NNNM", 120),     # 3N for 120, M is free
        ("RRRQ", 150),     # 3R for 150, Q is free
        ("UUUU", 120),     # 4U → 3U paid, 1U free
        ("PPPPP", 200),    # 5P for 200
        ("QQQ", 80),       # 3Q for 80
        ("VVV", 130),      # 3V for 130
        ("VV", 90),        # 2V for 90
    ]

    formatted_results = []
    for skus, expected in test_cases:
        actual = checkout(skus)
        result = "✅ PASSED" if actual == expected else f"❌ FAILED (Expected: {expected}, Got: {actual})"
        formatted_results.append(f"checkout({skus}) -> {actual} | {result}")

    # Print results
    for line in formatted_results:
        print(line)

# Run the formatted test cases
run_formatted_test_cases()





