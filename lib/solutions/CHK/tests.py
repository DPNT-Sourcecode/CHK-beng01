from checkout_solution import checkout
from checkout_solution import count_letters

aaa = "AAA"
aaabb = "AAABB"
mix = "ABCDE"
qwer = "qwer"
numbers = "1234"
lowercase = "abcd"

lowerUpper = "AaBbCcDd"



# print(count_letters(aaa))
# print(count_letters(aaabb))
# print(count_letters(qwer))
# print(count_letters(numbers))
# print(count_letters(mix))
# print(count_letters(lowercase))
# print(count_letters(lowerUpper))



# print(checkout("A"))
# print(checkout("B"))
# print(checkout("C"))
# print(checkout("D"))
# print(checkout("E"))


# print(checkout(aaa))
# print(checkout(mix))

# print(checkout("AAA")) #130
# print(checkout("AAAA")) 
# print(checkout("AAAAA"))
# print(checkout("AAAAAA"))
# print(checkout("AAAAAAA"))
# print(checkout("AAAAAAAA"))
# print(checkout("AAAAAAAAA"))
# print(checkout("AAAAAAAAAA"))
# print(checkout("AAAAAAAAAAA"))
# print(checkout("AAAAAAAAAAAA"))





# print(checkout("BB"))
# print(checkout("BBB"))
# print(checkout("BBBB"))
# print(checkout("EEB"))
# print(checkout("EEEEBB"))

# print(checkout(mix))


print(checkout("AABBCD"))   # Expected: 180
print(checkout("AAAAA"))    # Expected: 200
print(checkout("EEEEBB"))   # Expected: 160
print(checkout("EEEBBB"))   # Expected: 120 + 45 = 165
print(checkout("ABCDX"))    # Expected: -1 (invalid input)
print(checkout("FFFFFF"))   # Expected: 40 (6F → 4F paid, 2F free)
print(checkout("FFFFF"))    # Expected: 40 (5F → 4F paid, 1F free)
print(checkout("FFF"))      # Expected: 20 (3F → 2F paid, 1F free)
print(checkout("FFFAB"))    # Expected: 20 (3F) + 50 (A) + 30 (B) = 100

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







