#codewars

#1
def duplicate_encode(s):
    # Convert the input string to lowercase
    lower_s = s.lower()
    
    # Create a dictionary to count occurrences of each character
    char_count = {}
    for char in lower_s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Construct the result string based on character count
    result = ""
    for char in lower_s:
        if char_count[char] == 1:
            result += "("
        else:
            result += ")"
    
    return result

#2

def xor(a, b):
    return (a and not b) or (not a and b)

#მესამე ვერ გავიგე