# ====== Problem 4. Type-Conversion Detective =======

# Part A: Type Conversion
print("-"*30)
print(int("7") + 3.5)
print(str(10) * 3)
print(bool(""), bool(" "))
print(int(3.99))
print(float("1e3"))
print(int(True) + float("2.5"))
print(round(2.5), round(3.5))
print(type(10/2))

# Part B: A safe converter
def safe_int(text):
    """Turn text into an int; return None when it is not a number."""
    text = text.strip()     #strip() removes spaces at the beginning and end of text.
    if text.lstrip("-").isdigit():   # "42" or "-42"
        # lstrip("-") removes the - sign
        # isdigit() checks whether all remaining characters are digits (0–9)  
        return int(text)
    try:
        return int(float(text))   # "3.9" -> 3
    except ValueError:
        return None               # "abc", "", "12a"

print("-"*30)
for sample in ["42", "-8", "3.9", "abc", ""]:
    print(repr(sample), "->", safe_int(sample))
    # repr(sample) displays the text clearly, including quotation marks.


# Part C: Ask the user for two numbers with input(), convert them with safe_int() and print
print("-"*30)
num1 = safe_int(input("Enter first number: "))
num2 = safe_int(input("Enter second number: "))

if num1 is not None and num2 is not None:
    print("Sum = ", num1 + num2)
else:
    print("Please enter valid numbers!")

print("-"*30)














