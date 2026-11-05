# ====== Problem 3. Temperature Converter =======

def celsius_to_fahrenheit(c, round_to=1):
    """Convert degrees Celsius to degrees Fahrenheit."""
    return round(c * 9/5 +32 , round_to)

def fahrenheit_to_celsius(f, round_to=1):
    """Convert degrees Fahrenheit to degrees Celsius."""
    return round((f-32)* 5/9 , round_to)

# (a) Use a for loop with range(0, 101, 20) to print the conversion table below.
print("---- celsius_to_fahrenheit ----")
for c in range(0, 101, 20):
    print(f"{c:5} | {celsius_to_fahrenheit(c):6}")

# (b) Convert 98.6 °F (normal body temperature) to Celsius.
print("---- fahrenheit_to_celsius ----")
print("98.6 °F =", fahrenheit_to_celsius(98.6), "°C")

# (c) Convert 37 °C to Fahrenheit and back again. Do you get 37.0?
print("Round trip 37°C :", fahrenheit_to_celsius(celsius_to_fahrenheit(37)))

# (d) Call one function with round_to=3.
print("----- Custom Rounding -----")
print("25.6789 °C =", celsius_to_fahrenheit(25.6789, round_to=3), "°F")