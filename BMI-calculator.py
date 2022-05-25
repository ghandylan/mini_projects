# name = input("Hello! What can I call you? ")
# weight_kilograms = float(input(name + ", please enter your weight in kilos. "))
# height_meters = float(input(f'What is your height in meters, {name}? '))
# BMI = round(weight_kilograms/height_meters**2, 2)

# if BMI < 18.5:
#     print(f'{name}, your BMI is {BMI} \nYou are underweight. ')
# elif BMI <= 24.9:
#     print(f'{name}, your BMI is {BMI} \nYou are normal. ')
# elif BMI <= 29.9:
#     print(f'{name}, your BMI is {BMI} \nYou are overweight. ')
# elif BMI <= 34.9:
#     print(f'{name}, your BMI is {BMI} \nYou are obese. ')
# else:
#     print(f'{name}, your BMI is {BMI} \nYou are extremely obese. ')

def get_bmi(weight, height):
    BMI = (weight/height**2)
    print(BMI)
    if BMI < 18.5:
        return "underweight"
    elif BMI <= 24.9:
        return "normal"
    elif BMI <= 29.9:
        return "overweight"
    elif BMI <= 34.9:
        return "obese"
    else:
        return "extremely obese"


print(get_bmi(70, 1.7))
