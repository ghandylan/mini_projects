import os

def clear():
    os.system('cls')


def module_grade_average_2(m1, m2):
    return round((m1 + m2) / 2, 2)


def module_grade_average_3(m1, m2, m3):
    return round((m1 + m2 + m3) / 3, 2)


def transmute(module_grade_average):
    if module_grade_average >= 1 and module_grade_average <= 1.10:
        return 1
    elif module_grade_average >= 1.10 and module_grade_average <= 1.40:
        return 1.25
    elif module_grade_average >= 1.40 and module_grade_average <= 1.60:
        return 1.50
    elif module_grade_average >= 1.60 and module_grade_average <= 1.85:
        return 1.75
    elif module_grade_average >= 1.85 and module_grade_average <= 2.10:
        return 2.00
    elif module_grade_average >= 2.10 and module_grade_average <= 2.40:
        return 2.25
    elif module_grade_average >= 2.40 and module_grade_average <= 2.60:
        return 2.50
    elif module_grade_average >= 2.60 and module_grade_average <= 2.85:
        return 2.75
    elif module_grade_average >= 2.85 and module_grade_average <= 3.10:
        return 3.00
    else:
        return "IP"


def main():
    while True:
        # create a try/except block to catch the ValueError
        try:
            grades = []
            module_count = int(input("How many modules are there (2/3)? "))
            if module_count == 2:
                module_1 = float(input("Enter MODULE 1 grade: "))
                grades.append(module_1)
                module_2 = float(input("Enter MODULE 2 grade: "))
                grades.append(module_2)
                clear()
                if 5 in grades:
                    print("You got a grade of 5, please reach out to your professor.")
                else:
                    module_grade_average = module_grade_average_2(module_1, module_2)
                    print("The module grade average is: " + str(module_grade_average))
                    print("The transmuted grade is: " + str(transmute(module_grade_average)))
            elif module_count == 3:
                clear()
                module_1 = float(input("Enter MODULE 1 grade: "))
                grades.append(module_1)
                module_2 = float(input("Enter MODULE 2 grade: "))
                grades.append(module_2)
                module_3 = float(input("Enter MODULE 3 grade: "))
                grades.append(module_3)
                module_grade_average = module_grade_average_3(module_1, module_2, module_3)

                if 5 in grades:
                    print("You got a grade of 5, please reach out to your professor.")
                else:
                    print("The module grade average is: " + str(module_grade_average))
                    print("The transmuted grade is: " + str(transmute(module_grade_average)))
            else:
                clear()
                print("You have entered an invalid number of modules")
            
            # ask the user if they want to continue
            while True:
                continue_choice = input("Would you like to continue? (y/n): ")
                if continue_choice == "y":
                    clear()
                    break
                elif continue_choice == "n":
                    print("Have a nice day ????")
                    exit()
                else:
                    print("You have entered an invalid option")
                    continue

        except ValueError:
            clear()
            print("You have entered an invalid number")
            continue


main()