input_password = input("Enter a password: ")

# Variables
upper_count = 0
lower_count = 0
digit_count = 0
spec_count = 0
does_repeat = False
does_contain_simple_seq = False
seq = None
warning_req = 0
warning_sec = 0

# Important for later
spec_chars = """!~`@#$%^&*()_+-=\\{[}]|:;''""<,>.?/"""
simple_seq1 = "123"
simple_seq2 = "abc"
simple_seq3 = "qwerty"
simple_seq4 = "123456"
# Noted: Needs an even number of quotation marks, but it really doesnt change the objective.

# Analysis
for char in input_password:
    if "A" <= char <= "Z":
        upper_count += 1
    if "a" <= char <= "z":
        lower_count += 1
    if "0" <= char <= "9":
        digit_count += 1
    if char in spec_chars:
        spec_count += 1

# Repeated characters
for i in range(len(input_password) - 2):
    if (
        input_password[i] == input_password[i + 1]
        and input_password[i] == input_password[i + 2]
    ):
        does_repeat = True

# Simple Sequences(Just using 4)
if simple_seq1 in input_password:
    does_contain_simple_seq = True
    seq = simple_seq1
elif simple_seq2 in input_password:
    does_contain_simple_seq = True
    seq = simple_seq2
elif simple_seq3 in input_password:
    does_contain_simple_seq = True
    seq = simple_seq3
elif simple_seq4 in input_password:
    does_contain_simple_seq = True
    seq = simple_seq4

# Rating
if len(input_password) < 8:
    warning_req += 1

if upper_count == 0:
    warning_req += 1

if lower_count == 0:
    warning_req += 1

if digit_count == 0:
    warning_req += 1

if spec_count == 0:
    warning_req += 1

if does_repeat == True:
    warning_sec += 1

if does_contain_simple_seq == True:
    warning_sec += 1

rating = "Weak" if warning_req >= 1 else "Medium" if warning_sec >= 1 else "Strong"
feedback = None
if rating == "Weak":
    feedback = "- Missing Some Or All Requirements"
elif rating == "Medium":
    feedback = "- All Requirements Met But Some Potential Security Issues"
else:
    feedback = "- All Good To Go!"

# Analysis Output:

print("PASSWORD ANALYSIS:")
print("=" * 15)
print(f"Password: {input_password}")
print()
print("Character Counts:")
print(f"Length: {len(input_password)} characters")
print(f"Uppercase letters: {upper_count}")
print(f"Lowercase letters: {lower_count}")
print(f"Digits: {digit_count}")
print(f"Special characters: {spec_count}")
print()
print("Requirments Check:")
print(f"Length(8+ characters): {"✓ PASSED" if len(input_password) >= 8 else "⚠ WARNING"}")
print(f"Uppercase letters: {"✓ PASSED" if upper_count >= 1 else "⚠ WARNING"}")
print(f"Lowercase letters: {"✓ PASSED" if lower_count >= 1 else "⚠ WARNING"}")
print(f"Digits: {"✓ PASSED" if digit_count >= 1 else "⚠ WARNING"}")
print(f"Special Characters: {"✓ PASSED" if spec_count >= 1 else "⚠ WARNING"}")
print()
print("Security Issues:")
print(f"{"✓ No repeated characters in a row" if does_repeat == False else "⚠ WARNING, THERE IS ARE REPEATING CHARACTERS IN A ROW"} (3+)")
print(f"{"✓ No simple sequences" if does_contain_simple_seq == False else f"⚠ CONTAINS SEQUENCE '{seq}'"}")
print()
print(f"FINAL RATING: {rating}")
print(f"{feedback}")