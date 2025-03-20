room_length=float(input("Please enter the room's length in feets:\n"))
room_width=float(input("Please enter the room's width in feets:\n"))
if room_width<=0  and room_width <=0 :
    print("please enter a correct values")
#VARIABLES AND CONSTANTS
CONVERSION_FACTOR=0.092903
square_feet_area=room_length*room_width
square_meters_area=square_feet_area*CONVERSION_FACTOR
#END VARIABLES AND CONSTANTS
#AVOIDING THE FLOATING NUMBER
square_meters_area=round(square_meters_area,2)
square_feet_area=round(square_feet_area,2)
print(f"The surface area of the room in square feet is : {square_feet_area} ")
print(f"The surface area of the room in square meters is : {square_meters_area} ")