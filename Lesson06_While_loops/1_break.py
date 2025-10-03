# Break Statements in Loops
# break- exit the loop immediately.
# Use Cases:
"""
Stop when you find something
Exit early based on condition
Get out of infinite loops
"""

count = 1
while count <= 10:
    print(count)
    if count == 5:
        break
    count += 1


choice = input("Enter something(q for quit): ")
while True:
    if choice == "q":
        print("You wanted to exit")
        break
    print(f"You entered {choice}")
    
    