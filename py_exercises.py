while True:
    room_length = input("Please enter the room's length in feet:\n")
    room_width = input("Please enter the room's width in feet:\n")

    try:
        room_length = float(room_length)
        room_width = float(room_width)
    except ValueError:
        print("You should enter a valid number.")
        continue  # Loop again if there's a ValueError

    if room_length <= 0 or room_width <= 0:
        print("Please enter valid positive values for both dimensions.")
        continue  # Loop again if either dimension is non-positive

    # If input is valid, break the loop
    break

# VARIABLES AND CONSTANTS
CONVERSION_FACTOR = 0.092903
square_feet_area = room_length * room_width
square_meters_area = square_feet_area * CONVERSION_FACTOR
# END VARIABLES AND CONSTANTS

# AVOIDING THE FLOATING NUMBER
square_meters_area = round(square_meters_area, 2)
square_feet_area = round(square_feet_area, 2)

print(f"The surface area of the room in square feet is: {square_feet_area}")
print(f"The surface area of the room in square meters is: {square_meters_area}")