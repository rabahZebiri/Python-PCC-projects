#################### Serie 01  Ex01 ##########################
def ex_un():
    while True:
        try:
            x = float(input("PLease enter the first number : "))
            y = float(input("Please enter the second number : "))
        except ValueError:
            print("You should enter a numerical value !!")
        break

    equation_operator = input("Please enter the operator '+, - , * , / ,^ , % ' : ")

    if x.is_integer():
        x = round(x)
    if y.is_integer():
        y = round(y)

    if equation_operator == '*':
        result = x * y
    elif equation_operator == '/':
        result = x / y
    elif equation_operator == '^':
        result = x ** y
    elif equation_operator == '+':
        result = x + y
    elif equation_operator == '-':
        result = x - y
    elif equation_operator =='%':
        result =x % y
    else:
        print("Please enter a operator '+, - , * , / ,^ , % '")

    print(f"The result of the {x} {equation_operator} {y} is : {result}")

####################### Serie 01  Ex02 ##########################

def sum_in_range(start,end):
    """this function will calculate the sum of all the elements in  a specific range """
    if end >start :
        sum_inc=0
        for i in range(start,end+1):
            sum_inc=sum_inc+i

    if end <start :
        sum_inc=0
        for i in range(end,start+1):
            sum_inc=sum_inc+i

    print(f"The sum of the elements of the range [{start} ,{end}] is :{sum_inc}")

sum_in_range(4,-1)

#################### Serie 01  Exo3 #############################

numbers=[3,5,83,23,11,00,0.12,15,25,149.99,187,210,838,9,1]
def exo_3(numbers):
    for number in numbers :
        if number > 500 :
            break
        if number % 5 ==0 and number <=150 :
            print(number)

exo_3(numbers)

################### Serie 01  Exo4 ##############################

numbers_one=[5,10,15,20,25,30,35,40,45]
def reversing_list(numbers_list):
    for number in range(-1,-(len(numbers_list)+1),-1):
        print(numbers_list[number])

################### Exo5 ##############################

def factorial(number):
    fac=1
    for nmb in range(number,0,-1):
        fac=nmb*fac
    print(fac)

################### Serie 01  Exo6 ##############################

def cubes(number):
    '''This function calculates the cubes of each number of a defined range of numbers '''
    if number < 0:
        for nmb in range(0,number, -1):
            print(f"The cube of {nmb} is : {nmb ** 3}")

    else:
        for nmb in range(0, number + 1):
            print(f"The cube of {nmb} is : {nmb ** 3}")

################## Serie 01  Exo7 ###############################

numbers_list=[1,2,3,6,2,-3,0,22,1324,-0.5,23,111101,-868,0.0000134]
def odd_idex(numbers):
    out_list=[]
    for number in range(0,len(numbers)):
        if number%2 != 0 :
            out_list.append(numbers[number])
    print(out_list)

################## Serie 01  Exo 8 ##############################

def odd_even_checker():
    odd_list = []
    even_list = []
    while True:
        try:
            x = int(input("please enter how many numbers you want in your list : "))
        except ValueError:
            print("You should enter an integer !!")
        break
    if x < 0:
        print("You should enter a positive number :")

    for i in range(0, x):
        val= int(input("Please enter a number : "))
        if val % 2 == 0:
            even_list.append(val)
        elif val % 2 != 0:
            odd_list.append(val)

    print(f"\nThe odd numbers are : {odd_list}\n")
    print(f"The even numbers are : {even_list}")

#######################################################################################################################
                            ######Serie 02(fonctions)##########