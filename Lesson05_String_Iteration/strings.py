# word = "Python"
#         012345   positive indexing
#        -654321   negative indexing

# length-1=last character
# -length = last character

# Slicing => string[start:stop]
# [:stop] => starts at 0
# [start:] => from designated index to the end
# [-start] => last few chracters
# [::-1] => reverse


# String Indexing and Slicing
word = "Python"

word[0] # P
word[1] # y
word[5] # n
word[-1] # n
len(word) #length
word[len(word)-1] # n

# Slicing

word[0:3] #Pyt
word[:3] #Pyt
word[2:5] #tho
word[2:6] #thon
word[2:len(word)] #thon
word[2:] #thon
word[-3:] #hon

# Part 1 - string iteration

word2 = "hello"

for char in word2:
    print(char)
    
for i in range(len(word2)):
    print(f"Character {i}: {word2[i]}")
    
# Character classification
# char = "A"
char = input('Press a key: ')

if "A" <= char <= "Z":
    print(f"'{char}' is uppercase")
    
if "a" <= char <= "z":
    print(f"'{char}' is lowercase")
    
if "0" <= char <= "9":
    print(f"'{char}' is a digit")
    
if "A" <= char <= "Z" or "a" <= char <= "z":
    print(f"'{char} is a letter'")