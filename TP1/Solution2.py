# ====== Problem 2. Time Converter =======

# (a). Compute hours, minutes and seconds, then print the sentence shown below.
total_seconds = 9875

hour = total_seconds // 3600
minute = (total_seconds % 3600) // 60
second = total_seconds % 60

print(f"{total_seconds} seconds = {hour}h {minute}min {second}s")

# (b). Check your answer: rebuild the total from the three parts and print whether it equals total_seconds.
result_seconds = (hour * 3600) + (minute * 60) + (second)
print("------ Check Result -----")
print(f"Original seconds : {total_seconds}")
print(f"Result seconds : {result_seconds}")
print(f"Check : {result_seconds == total_seconds}")
print(f"-"*26)

# (c). Test your code with 3600, 59 and 86399 seconds.
test_values = [3600, 59, 86399]

for total_seconds in test_values:
    hour = total_seconds // 3600
    minute = (total_seconds % 3600) // 60
    second = total_seconds % 60

    print(f"{total_seconds} seconds = {hour}h {minute}min {second}s")
