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

print(checkout("AABBCD"))   # 180 = 100 + 45 + 20 + 15
print(checkout("AAAAA"))    # 200
print(checkout("EEEEBB"))   # 160
print(checkout("EEEBBB"))   # 165
print(checkout("ABCDX"))    # 50 + 30 + 20 + 15 + 90 = 205
print(checkout("FFFFFF"))   # 40 (6F → 4F paid, 2F free)
print(checkout("FFFFF"))    # 40 (5F → 4F paid, 1F free)
print(checkout("FFF"))      # 20 (3F → 2F paid, 1F free)
print(checkout("NNNM"))     # 120 (3N for 120, M is free)
print(checkout("RRRQ"))     # 150 (3R for 150, Q is free)
print(checkout("UUUU"))     # 120 (4U → 3U paid, 1U free)
print(checkout("PPPPP"))    # 200 (5P for 200)
print(checkout("QQQ"))      # 80 (3Q for 80)
print(checkout("VVV"))      # 130 (3V for 130)
print(checkout("VV"))       # 90 (2V for 90)
print(checkout("HHHHH"))    # 45 (5H for 45)
print(checkout("HHHHHHHHHH"))  # 80 (10H for 80)
print(checkout("HHHHHHHHHHH")) # 90 (10H for 80 + 1H for 10)


