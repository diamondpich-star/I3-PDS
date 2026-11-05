# ====== Problem 1. Student Profile Card =======
# Create five variables
name = "Sok Dara"
age = 20
major = "Data Science"
gpa = 3.67
is_scholar = True

# (a). Print student profile card
print("=" * 30)
print(f"Name : {name}")
print(f"Age : {age}")
print(f"Major : {major}")
print(f"GPA : {gpa:.2f}")
print(f"Scholar : {is_scholar}")
print("=" * 30)

# (b). Print values and their data types
print(f"'{name}'-> {type(name).__name__}")
print(f"'{age}'-> {type(age).__name__}")
print(f"'{major}'-> {type(major).__name__}")
print(f"'{is_scholar}'-> {type(is_scholar).__name__}")

# (c). Re-assign age
age = "20"
print(f"After ressigment the age -> {type(age).__name__}")