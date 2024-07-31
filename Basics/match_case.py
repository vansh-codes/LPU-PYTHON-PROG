def classify_number(x):
    match x:
        case 0:
            return "Zero"
        case 1 | 2 | 3:
            return "Small"
        case int if int > 3 and int < 10:
            return "Medium"
        case int if int >= 10:
            return "Large"
        case _:
            return "Unknown"

print(classify_number(0))    # Output: Zero
print(classify_number(2))    # Output: Small
print(classify_number(5))    # Output: Medium
print(classify_number(15))   # Output: Large
print(classify_number("abc")) # Output: Unknown
