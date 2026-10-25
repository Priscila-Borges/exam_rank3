"""
Problem 10: Number Base Conversion
Write a function that converts a number from one base to another.
Support bases from 2 to 36 inclusive.
Use digits 0-9 and letters A-Z for values 10-35.
Return "ERROR" for invalid inputs.

Function signature
def number_base_converter(number: str, from_base: int, to_base: int) -> str:
"""

# FUNCTION number_base_converter(number, from_base, to_base):

#     # 1. SETUP: Create our dictionary of all possible digits (0-9, A-Z)
#     DEFINE digits AS "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#     # 2. VALIDATION: Check if bases are within the allowed range (2 to 36)
#     IF from_base is NOT between 2 and 36:
#         RETURN "ERROR"
#     IF to_base is NOT between 2 and 36:
#         RETURN "ERROR"

#     # 3. PARSE IN: Convert the input string into a standard decimal (base 10) number
#     # (Wrap this in a try/except block because invalid characters will crash it)
#     TRY:
#         decimal = CONVERT number TO integer using from_base
#     EXCEPT error:
#         RETURN "ERROR"

#     # 4. EDGE CASE: If the number is 0, just return "0"
#     IF decimal == 0:
#         RETURN "0"

#     # 5. CONVERT OUT: Transform the decimal number into the target base
#     DEFINE result AS empty string

#     WHILE decimal is greater than 0:
#         # Find the remainder to get the last digit's value
#         remainder = decimal MODULO to_base
        
#         # Look up that value in our digits string and add it to the FRONT of our result
#         result = digits[remainder] + result
        
#         # Shrink the decimal number using floor division
#         decimal = decimal DIVIDED BY to_base (rounded down)

#     # 6. Return the final converted string
#     RETURN result

# def number_base_converter(number: str, from_base: int, to_base: int) -> str:
# 	digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 	if not 2 <=  from_base <= 36:
# 		return "ERROR"
# 	if not 2 <= to_base <= 36:
# 		return "ERROR"

# 	try:
# 		decimal = int(number, from_base)
# 	except ValueError:
# 		return "ERROR"
# 	if decimal == 0:
# 		return "0"	
# 	result: str = ""
# 	while decimal > 0:
# 		remainder = decimal % to_base
# 		result = digits[remainder] + result
# 		decimal = decimal // to_base
# 	return result	


def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if not 2 <= from_base <= 36:
        return "ERROR"
    if not 2 <= to_base <= 36:
        return "ERROR"
    try:
        decimal = int(number, from_base)
    except ValueError:
        return "ERROR"
    if decimal == 0:
        return "0"
    result: str = ""
    while decimal > 0:
        result = digits[decimal % to_base] + result
        decimal //= to_base
    return result


print(number_base_converter("1010", 2, 10))  # 10
print(number_base_converter("255", 10, 16))  # FF
print(number_base_converter("123", 1, 10))  # ERROR
