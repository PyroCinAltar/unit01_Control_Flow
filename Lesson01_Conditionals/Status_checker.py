# Student Information System - Starter Code

print("STUDENT INFORMATION SYSTEM")
print("========================================")

# Get student information
name = input("Enter student name: ")
age = int(input("Enter student age: "))
gpa = float(input("Enter student GPA (0.0-4.0): "))

# Show student information
print()
print("Student Information:")
print("Name:", name)
print("Age:", age)
print("GPA:", gpa)
print()
print("Eligibility Status:")

# TODO: Check if age is valid (between 16 and 100)
if 16 <= age <= 100:
    

# TODO: Check if GPA is valid (between 0.0 and 4.0)
    if 0.0 <= gpa <= 4.0:

# TODO: Check enrollment eligibility (age >= 18 AND gpa >= 2.0)
        if age >= 18 and gpa >= 2.0:
            print('✅ ELIGIBLE for enrollment')
        else:
            print("❌ NOT ELIGIBLE for enrollment")
            
# TODO: Check voting eligibility (age >= 18)
        if age >= 18: 
            print('✅ ELIGIBLE to vote')
        else:
            print("❌ NOT ELIGIBLE to vote")
            

# TODO: Check honor roll status (gpa >= 3.5)

        if gpa >= 3.5:
            print("🏆On honor roll")
        else:
            print("Not on honor roll")

    else:
        print("Please enter a valid GPA score")
else:
    print('Please enter a valid age')