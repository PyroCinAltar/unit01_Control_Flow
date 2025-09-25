# variable = "True value" if "condition" else "False value"

# JS Ternary
"""
let status = age >= 18 ? "adult" : "minor"
let message = score >= 90 ? "Excellent" : "Keep Trying"
"""

# Pyhton Ternary
age = 15
status = "adult" if age >= 18 else "minor"
score = 75
message = "Excellent" if score >= 90 else "Keep Trying"

# Examples
password = "mypass123"

strength = "Strong" if len(password) >= 18 else "Weak"
print(f"Password: {password}\nStrength: {strength}") 

# Combining Ternaries + Chaining
category = ('Child' if 0 <= age <= 12 else "Teen" if 13 <= age <= 17 else "Adult" if 18<= age <= 64 else "Senior")

grade = 89

grade = ("A" if 90 <= grade <= 100 else "B" if 80 <= grade < 90 else "C" if 70 <= grade < 80 else "D" if 60 <= grade < 70 else "F")