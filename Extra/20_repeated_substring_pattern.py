"""
Given a string s, check if it can be constructed by taking a substring of it and appending
multiple copies of the substring together.

Examples:
"abab" → True (substring "ab" repeated twice)
"aba" → False
"abcabcabcabc" → True (substring "abc" repeated 4 times)
"aaa" → True (substring "a" repeated 3 times)
"""

def repeated_substring_pattern(s: str) -> bool:
    n = len(s)
    
    # Try all possible substring lengths from 1 up to half the string's length
    for i in range(1, n // 2 + 1):
        # Check if this length evenly divides the total length
        if n % i == 0:
            substring = s[:i]
            multiplier = n // i
            
            # If repeating this substring recreates s, we found a match!
            if substring * multiplier == s:
                return True
                
    return False

# Test cases
print(repeated_substring_pattern("abab"))          # True ("ab" repeated 2 times)
print(repeated_substring_pattern("aba"))           # False
print(repeated_substring_pattern("abcabcabcabc"))  # True ("abc" repeated 4 times)
print(repeated_substring_pattern("aaa"))           # True ("a" repeated 3 times)
