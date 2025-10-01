# Syntax
"""
while condition:
    code block

"""

# import time

# num = 5
# while num > 0:
#     print(num)
#     num -= 1
#     time.sleep(1)
# print("BLAST OFF!")

# sum = 0
# num = 1

# while num <= 10:
#     sum += num
#     num += 1

# print(f"Sum of numbers from 1 - 10: {sum}")

# while num <= 10:
#     sum += num
#     if num < 10:
#         print(num, end ="+")
#     else:
#         print(num, end="=")
#     num += 1


# Sum of digits
# take user input as int, nd sum the digits of it.
n = input("Please enter a number: ")


sum = 0

for char in n:
    sum += int(char)
print(f"Total: {sum}")

sum2 =0
i = 0

while i < len(n):
    sum2 += int(n[i])
    i+=1
print(f"Total: {sum2}")

