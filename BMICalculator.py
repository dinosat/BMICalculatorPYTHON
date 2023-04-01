height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = weight/(height **2)

if bmi < 18.5:
    bmi_category = "Underweight"
elif bmi >= 18.5 and bmi <25:
    bmi_category = "Normalweight"
elif bmi >= 25 and bmi <30:
    bmi_category = "Overweight"
else:
    bmi_category = "Obese"


print("Your BMI is:" , round(bmi,2), "\n", "You are" , bmi_category)