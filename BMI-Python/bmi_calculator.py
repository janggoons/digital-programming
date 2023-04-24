# BMI Calculator with detailed output

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100  # convert height from cm to m
    bmi = weight / (height_m ** 2)
    return bmi

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

weight = float(input("Enter your weight in kilograms: "))
height_cm = float(input("Enter your height in centimeters: "))

bmi = calculate_bmi(weight, height_cm)
bmi_category = get_bmi_category(bmi)

print(f"Your BMI is: {bmi:.2f}")
print(f"Your weight is {bmi_category}.")
