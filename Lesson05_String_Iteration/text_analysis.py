text = input("Enter a text:")
total_chars = len(text)
letter_count = 0
digit_count = 0
upper_count = 0
lower_count = 0

first_letter = None
last_letter = None

print(f"Analyzing: {text}")
print("=" * 40)

# process each character

for char in text:
    if "A" <= char <= "Z" or "a" <= char <= "z":
        letter_count += 1
        if first_letter == None:
            first_letter = char
        last_letter = char
    if "A" <= char <= "Z":
        upper_count += 1
    if "a" <= char <= "z":
        lower_count += 1
    if "0" <= char <= "9":
        digit_count += 1

print(f"Total characters: {total_chars}")
print(f"Letters: {letter_count}")
print(f"Digits: {digit_count}")
print(f"Uppercase Letters: {upper_count}")
print(f"lowercase: {lower_count}")
print(f"First letter: {first_letter}")
print(f"last letter: {last_letter}")