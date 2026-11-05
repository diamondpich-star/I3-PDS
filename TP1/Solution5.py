# ====== Problem 5. Letter Grade =======

def letter_grade(score):
    if score < 0 or score > 100:
        return("Invalid!")
    elif score >= 97:
        return "A+"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# (a)Test your function with the list [99, 90, 85.5, 72, 60, 59.9, -5, 101] and print the results aligned as below
scores = [99, 90, 85.5, 72, 60, 59.9, -5, 101]

for score in scores:
    print(f"{score:5} -> {letter_grade(score)}")



# (b) Why must the test for A+ come before the test for A? What happens if you swap them?
# A+ must come before A because the condition score >= 97 is more specific than score >= 90.
# If we put A before A+, a score of 99 will satisfy score >= 90 first. 
# Python will return "A" immediately and will not check the A+ condition. Therefore, the result will be incorrect.
# Example
def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 97:
        return "A+"
    else:
        return "Other"
    
print("Example part B")
print(f"99 -> {letter_grade(99)}")
