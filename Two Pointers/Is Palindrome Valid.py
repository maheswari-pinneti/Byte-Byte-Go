import re

def is_palindrome_valid(s: str) -> bool:
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    
    # Check if the cleaned string is a palindrome
    return cleaned_s == cleaned_s[::-1]

# Test cases
print(is_palindrome_valid('a dog! a panic in a pagoda.'))  # Output: True
print(is_palindrome_valid('abc123'))  # Output: False

