weight = float(input("Put your weight in pounds please:"))
height = float(input("Put your height in inches pleasse:"))


def calcBMI():
    BMI = 703 * weight / height**2
    if BMI > 39.9:
        condition = "Morbidy Obese"
    elif BMI >= 35:
        condition = "Very Obese"
    elif BMI >= 29.9:
        condition = "Obese"
    elif BMI >= 25:
        condition = "Overweight"
    elif BMI >= 18.5:
        condition = "Normal"
    else:
        condition = "Underweight"
    print("Your BMI is {:0.1f}".format(BMI) + ". \nYou are " + condition + ".")

calcBMI()

