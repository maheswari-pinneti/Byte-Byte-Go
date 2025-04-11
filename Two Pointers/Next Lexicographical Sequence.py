def next_lexicographical_sequence(s: str) -> str:
    # Convert string to list for easy swapping
    arr = list(s)
    n = len(arr)
    
    # Step 1: Find pivot
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    
    # If no pivot found, return the smallest order (sorted string)
    if i == -1:
        return ''.join(sorted(arr))
    
    # Step 2: Find the smallest character on the right that is larger than arr[i]
    j = n - 1
    while arr[j] <= arr[i]:
        j -= 1
    
    # Step 3: Swap arr[i] and arr[j]
    arr[i], arr[j] = arr[j], arr[i]
    
    # Step 4: Reverse the substring from i+1 to end
    arr[i + 1:] = reversed(arr[i + 1:])
    
    return ''.join(arr)

# Test cases
print(next_lexicographical_sequence("abcd"))  # Output: "abdc"
print(next_lexicographical_sequence("dcba"))  # Output: "abcd"
