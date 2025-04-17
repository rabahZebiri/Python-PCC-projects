while True:
    try:
        rooms_length=float(input("PLease enter the length of the room in feet : "))
        rooms_width=float(input("Please enter the width of your room in feets : "))
    except ValueError :
        print("PLease enter a numerical numbers !!")

    if rooms_width <=0 or rooms_length <=0 :
        print("PLease check your values !!")
    break

if rooms_width.is_integer() :
    rooms_length=round(rooms_length)
if rooms_width.is_integer() :
    rooms_width=round(rooms_width)

CONVERSION_FACTOR = 0.092903
square_feet_area=rooms_width*rooms_width
square_meter_area=square_feet_area*CONVERSION_FACTOR

print(f"The surface area of your room in square feets is : {square_feet_area}")
print(f"The surface area of your room in square meters is : {square_meter_area}")