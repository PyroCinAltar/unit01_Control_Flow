height = input("Please enter your height in inches: ")
weight = input("Please enter your height in pounds: ")

if height and weight:
    height_int = int(height)
    weight_int = int(weight)
    
    calculate = (weight_int / height_int**2) * 703

    categorize
    
else:
    print("Please enter a valdi height")