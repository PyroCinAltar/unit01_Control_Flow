print("=== BMI Calculator ===")
height = input("Please enter your height in inches: ")
weight = input("Please enter your height in pounds: ")


if height and weight:
    height_int = float(height)
    weight_int = float(weight)
    
    bmi = (weight_int / height_int**2) * 703
    categorize = "Underweight" if bmi < 18.5 else "Normal" if 18 <= bmi < 25 else "Overweight" if 25 <= bmi < 30 else "Obese"
    risk = "Low" if categorize == "Normal" else "Moderate" if categorize == 'Overweight' else "High" if categorize == "Underweight" else "Severe"
    recom = "Maintain weight" if categorize == "Normal" else "Gain weight" if categorize == "Underweight" else "Lose weight" if categorize == 'Overweight' else "Seek Treatment"
    
    print("===================================")
    print("BMI Health Report")
    print("===================================")
    print(f'Height: {height_int}"')
    print(f"Weight: {weight_int} .lbs")
    print(f"BMI: {bmi:1f }")
    print(f"Category: {categorize}")
    print(f"Recommendation: {recom}")
    print(f"Health Risk: {risk}")
    print("===================================")
    
else:
    print("Please enter positive values")