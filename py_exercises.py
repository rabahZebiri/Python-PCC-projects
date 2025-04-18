####################   Ex01 ##########################
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

####################### Ex02 ##########################

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

#################### Exo3 #############################

numbers=[3,5,83,23,11,00,0.12,15,25,149.99,187,210,838,9,1]
def exo_3(numbers):
    for number in numbers :
        if number > 500 :
            break
        if number % 5 ==0 and number <=150 :
            print(number)

exo_3(numbers)

################### Exo4 ##############################

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

################### Exo6 ##############################

