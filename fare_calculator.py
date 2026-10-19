# Travel Fare Calculator
FARE_RATE = 14

#Validate passenger name
while True:
    name = input("Enter passenger name: ")
    if name.strip() != "":
        break
    else:
        print("Invalid name. Name cannot be blank.")

#Validate distance
while True:
    try:
        distance = float(input("Enter distance (km): "))
        if distance > 0:
            break
        print("Invalid distance. Enter a number greater than 0.")
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")

#Validate number of passengers
while True:
    try:
        passengers = int(input("Enter number of passengers: "))
        if passengers > 0:
            break
        print("Invalid number of passengers. Enter a positive whole number.")
    except ValueError:
        print("Invalid input. Please enter a valid whole number.")

total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))
