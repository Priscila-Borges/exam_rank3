# Problem 6: Whisper Cipher (Caesar Cipher)
# Write a function that shifts alphabetical characters by a given amount.

# Only shift letters (a-z, A-Z)
# Preserve case
# Other characters remain unchanged
# Wraparound: 'z' + 1 = 'a'
# Examples:
# "hello", shift=3 → "khoor"
# "hello world!", shift=3 → "khoor zruog!"
# "xyz", shift=3 → "abc"
# "ABC", shift=1 → "BCD"