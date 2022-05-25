def main():
    print('PYNATIVE BEGINNER EXERCISES\n')
main()

def exercise_1():
    print('Exercise 1:')
    number1 = 40
    number2 = 30
    product = number1*number2
    add = number1+number2
    if product > 1000:
        print(f'The result is {add}')
    else:
        print(f'The result is {product}')
exercise_1()

def exercise_2():
    print('\nExercise 2:')
    for number in range(0, 10):
        current_number = number
        previous_number = number-1
        if previous_number == -1:
            previous_number = 0
        sum_of_numbers =current_number+previous_number
        if sum_of_numbers == -1:
            sum_of_numbers == 0
        print(f'Current number: {current_number}  Previous number:{previous_number}  Sum: {sum_of_numbers}')
exercise_2()

def exercise_3():
    str = 'pynative'
    print(f'\nExercise 3:\nOriginal string is {str}\nPrinting only even index characters')
    str = 'Pynative'
    for num in range(0,len(str),2):
        print(str[num])

exercise_3()

def exercise_4():
    print('Not yet done.\n')
exercise_4()

def exercise_5():
    print('Exercise 5:')
    list1 = [900,20,10,30,10]
    print(list1)
    if list1[-1] == list1[0]:
        print('result is True')
    else:
        print('result is False')
    list2 = [20,50,45,10,60]
    print(list2)
    if list2[-1] == list2[0]:
        print('result is True')
    else:
        print('result is False')
exercise_5()

def exercise_6():
    print('\nExercise 6:\nDivisible by 5 in list')
    list = [1,2,5,10,30,23,12,46,25]
    print(f'Given list is {list}')
    for number in list:
        if number % 5 == 0:
            print(number)
exercise_6()

def exercise_7():
    print('\nExercise 7:')
    str = "Her name is Emma Emma likes apples. Emma is from the city. Emma is good developer. Emma is a writer.".split()
    str_count = 0
    for word in str:
        if 'Emma'.casefold() in word.casefold():
            str_count += 1
    print(f'Emma appeared {str_count} times')
exercise_7()

def exercise_8():
    print('\nExercise 8:')
    count = 0
    x = 0
    y = 1
    z = 0
    while count < 10:
        count += 1
        x += 1
        y += 10
        z += 1
        print('')
        for number in range(x,y,z):
            print(" ",number, end='\t')
        
exercise_8()
