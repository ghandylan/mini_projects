class Calculator:
    def add (self, a, b):
        return a + b
    def subtract (self, a, b):
        return a - b
    def multiply (self, a, b):
        return a * b
    def divide (self, a, b):
        if b == 0: 
            return "undefined" 
        else: 
            return a/b 

calculate = Calculator()

def cls(): 
    print ("\n" * 100)
    
def continueQuery():
    cont = str(input("Do you want to continue? [Y/N]: "))
    if cont.upper() == "Y".upper():
        cls()
        main()
    elif cont.upper() == "N".upper():
        print("Closing program...")
        exit()
    else:
        print("Invalid choice, please enter again.")
        continueQuery()

def main():
    cls()
    while True:
        print('''
Arithmetic Calculator
[1] Add
[2] Subtract
[3] Multiply
[4] Divide
[5] Exit
    ''')
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            cls()
            print("Please enter an integer.")
        else:
            if choice == 5:
                print("Closing program...")
                quit()         
            if choice in [1,2,3,4]:
                cls()
                while True:
                    try:
                        a = int(input("Enter first number: "))
                    except ValueError:
                        print("Please enter an integer.")
                        continue
                    else:
                        break
                while True:
                    try:
                        b = int(input("Enter second number: "))
                    except ValueError:
                        print("Please enter an integer.")
                        continue
                    else:
                        break                
                if choice == 1:
                    print(f"{a} + {b} = {calculate.add(a,b)}")
                elif choice == 2:
                    print(f"{a} - {b} = {calculate.subtract(a,b)}")
                elif choice == 3:
                    print(f"{a} * {b} = {calculate.multiply(a,b)}")
                elif choice == 4:
                    print(f"{a} / {b} = {calculate.divide(a,b)}")
                
                continueQuery()              
            else:
                cls()
                print("Invalid choice.")
                continue


main()