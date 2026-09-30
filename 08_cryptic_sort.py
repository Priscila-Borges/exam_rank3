# Problem 8: Cryptic Sort
# Write a function that sorts a list of strings according to multiple criteria:

# Primary sort: Length (shortest first)
# Secondary sort: Alphabetically (if same length)
# Tertiary sort: Number of vowels (fewest first, if still tied)
# Requirements:

# Handle empty strings and lists
# Treat mixed case as lowercase for comparison
# Ignore special characters when counting vowels
# Vowels are: a, e, i, o, u
# Examples:
# ["apple", "pie", "a"] → ["a", "pie", "apple"]
#   (lengths: 1, 3, 5)

# ["dog", "cat", "bee"] → ["bee", "cat", "dog"]
#   (same length 3, alphabetically: bee < cat < dog)

# ["aaa", "eee", "bbb"] → ["bbb", "aaa", "eee"]
#   (same length 3, alphabetically same group, vowel counts: 0, 3, 3)