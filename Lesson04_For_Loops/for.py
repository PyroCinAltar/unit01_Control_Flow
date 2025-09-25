# Three froms of range() function
# range(stop)
for i in range(5):
    print(i)
print()
# range(start,stop) 
for i in range(3, 8):
    print(i)
print()


# range(start, stop, step)
for i in range(2, 11, 2):
    print(i)
print()

# Counting backwards
for i in range(10, 1, -2):
    print(i)
print()
    

# People do this
# for _ in range(5):
# _ is a dummy variable.
# Is used when people dont need the variable, only the looping.

# Countdown timer
import time
for sec in range(10, -1, -1):
    print(f"Seconds: {sec}")
    time.sleep(1)
print("Blast Off!")

# Multiplication table
# User input for number and print the table from 1-10

num = int(input("Enter the number(1-12): "))
if 1 <=  num <= 12:
    for i in range(1, 11):
        print(f"{num} * {i:2d} = {(num * i):3d}")
    time.sleep(1)
else:
    print("Please enter a number from 1-12")